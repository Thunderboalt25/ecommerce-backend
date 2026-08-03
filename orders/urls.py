from django.urls import path


from .views import (
    CheckoutView,
    OrderHistoryView,
    OrderDetailView,
    CancelOrderView,
)

urlpatterns = [

    path(
        "",
        OrderHistoryView.as_view(),
        name="order-history"
    ),

    path(
        "checkout/",
        CheckoutView.as_view(),
        name="checkout"
    ),

    path(
    "<int:pk>/",
    OrderDetailView.as_view(),
    name="order-detail"
    ),

    path(
    "<int:pk>/cancel/",
    CancelOrderView.as_view(),
    name="cancel-order"
    ),
]