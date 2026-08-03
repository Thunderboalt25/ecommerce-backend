from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):

    serializer_class = ReviewSerializer

    permission_classes = [IsAuthenticated]

    queryset = Review.objects.all()

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)