from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer, ProductCreateSerializer


class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    filterset_fields = ["category"]

    search_fields = ["name", "description"]

    ordering_fields = ["price", "created_at"]

    def get_serializer_class(self):

        if self.action in ["create", "update", "partial_update"]:
            return ProductCreateSerializer

        return ProductSerializer