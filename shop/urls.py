from django.urls import path
from .views import ProductSingleView, ShopView


app_name = "shop"

urlpatterns = [
    path('product-single/', ProductSingleView.as_view(), name='product-single'),
    path('', ShopView.as_view(), name='shop'),
]
