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

    class Meta:

        model = CartItem

        fields = ["id", "product", "quantity"]    

class CartReadSerializer(serializers.ModelSerializer):

    items = CartItemReadSerializer(many=True)

    class Meta:

        model = Cart

        fields = ["id", "user", "items"]        