from django.urls import path
from .views import IndexShopView, AboutView, ContactView


app_name = "home"

urlpatterns = [
  path('', IndexShopView.as_view(), name="index"),# Пустая строка означает, что название пути будет соединяться с корневым путем загружаемым из корневого маршрута.
  path('about/', AboutView.as_view(), name='about'),
  path('contact/', ContactView.as_view(), name='contact'),
]
