from django.urls import path

from .views import AddToCartView
from .views import AddToCartView, MyCartView

urlpatterns = [

    path(
        "add/",
        AddToCartView.as_view(),
        name="add-cart"
    ),

path(
    "",
    MyCartView.as_view(),
    name="my-cart"
),
]