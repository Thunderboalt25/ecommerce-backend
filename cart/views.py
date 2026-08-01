from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Cart, CartItem
from .serializers import (
    AddToCartSerializer,
    CartReadSerializer,
)
from products.models import Product


class AddToCartView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = AddToCartSerializer(data=request.data)

        if serializer.is_valid():

            product = Product.objects.get(
                id=serializer.validated_data["product"]
            )

            cart, created = Cart.objects.get_or_create(
                user=request.user
            )

            cart_item, created = CartItem.objects.get_or_create(
                cart=cart,
                product=product,
                defaults={
                    "quantity": serializer.validated_data["quantity"]
                }
            )

            if not created:

                cart_item.quantity += serializer.validated_data["quantity"]

                cart_item.save()

            return Response(
                {
                    "message": "Product Added To Cart"
                },
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class MyCartView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        cart = Cart.objects.get(
            user=request.user
        )

        serializer = CartReadSerializer(cart)

        return Response(serializer.data)    