from django.shortcuts import render
from django.views import View


class ViewCart(View):
    def get(self, request):
        return render(request, 'cart/cart.html')


class WishlistView(View):
    def get(self, request):
        return render(request, 'cart/wishlist.html')
