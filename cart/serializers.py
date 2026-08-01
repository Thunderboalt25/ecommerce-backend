from rest_framework import serializers

from .models import Cart, CartItem


class CartSerializer(serializers.ModelSerializer):

    class Meta:

        model = Cart

        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):

    class Meta:

        model = CartItem

        fields = "__all__"


class AddToCartSerializer(serializers.Serializer):

    product = serializers.IntegerField()

    quantity = serializers.IntegerField(default=1) 

           
class CartItemReadSerializer(serializers.ModelSerializer):

    product = serializers.StringRelatedField()

    price = serializers.ReadOnlyField(source="product.price")

    subtotal = serializers.SerializerMethodField()

    class Meta:

        model = CartItem

        fields = [
            "id",
            "product",
            "price",
            "quantity",
            "subtotal",
        ]

    def get_subtotal(self, obj):

        return obj.product.price * obj.quantity    



class CartReadSerializer(serializers.ModelSerializer):

    items = CartItemReadSerializer(
        many=True
    )

    total = serializers.SerializerMethodField()

    class Meta:

        model = Cart

        fields = [
            "id",
            "user",
            "items",
            "total",
        ]

    def get_total(self, obj):

        total = 0

        for item in obj.items.all():

            total += item.product.price * item.quantity

        return total       