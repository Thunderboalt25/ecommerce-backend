from decimal import Decimal

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from cart.models import Cart
from .models import Order, OrderItem
from .serializers import OrderSerializer


class CheckoutView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        cart = Cart.objects.get(user=request.user)

        cart_items = cart.items.all()

        total = Decimal("0.00")

        order = Order.objects.create(
            user=request.user
        )

        for item in cart_items:

            subtotal = item.product.price * item.quantity

            total += subtotal

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
                subtotal=subtotal
            )

        order.total = total

        order.save()

        cart.items.all().delete()

        serializer = OrderSerializer(order)

        return Response(serializer.data)

class OrderHistoryView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        orders = Order.objects.filter(
            user=request.user
        ).order_by("-created_at")

        serializer = OrderSerializer(
            orders,
            many=True
        )

        return Response(serializer.data)    

class OrderDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):

        order = Order.objects.get(
            id=pk,
            user=request.user
        )

        serializer = OrderSerializer(order)

        return Response(serializer.data)    

class CancelOrderView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        order = Order.objects.get(
            id=pk,
            user=request.user
        )

        order.status = "Cancelled"

        order.save()

        return Response(
            {
                "message": "Order Cancelled Successfully"
            }
        )    