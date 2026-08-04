from rest_framework import serializers

from .models import Product
from categories.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_image(self, obj):
        request = self.context.get("request")

        if obj.image:
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url

        return None


class ProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"