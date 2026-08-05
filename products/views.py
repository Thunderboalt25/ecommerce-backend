from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer, ProductCreateSerializer

from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated

class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all().order_by("-created_at")

    serializer_class = ProductSerializer

    permission_classes = [IsAdminOrReadOnly]

    filterset_fields = ["category"]

    search_fields = ["name", "description"]

    ordering_fields = ["price", "created_at"]

    def get_serializer_class(self):

        if self.action in ["create", "update", "partial_update"]:
            return ProductCreateSerializer

        return ProductSerializer