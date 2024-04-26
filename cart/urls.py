from django.urls import path
from .views import ViewCart, WishlistView


app_name = "cart"

urlpatterns = [
    path('', ViewCart.as_view(), name='cart'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),

]
