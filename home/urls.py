from django.urls import path
from .views import IndexShopView


app_name = "home"

urlpatterns = [
  path('', IndexShopView.as_view(), name="index"),# Пустая строка означает, что название пути будет соединяться с корневым путем загружаемым из корневого маршрута.


]
