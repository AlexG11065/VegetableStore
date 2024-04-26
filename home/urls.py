from django.urls import path


from .views import IndexShopView


urlpatterns = [
  path('', IndexShopView.as_view()),# Пустая строка означает, что название пути будет соединяться с корневым путем загружаемым из корневого маршрута.


]
