from django.urls import path

from .views import catalog, orders, order_create, product_detail

app_name = "shop"

urlpatterns = [
    path("", catalog, name="catalog"),
    path("orders", orders, name="orders"),
    path("order_create", order_create, name="order_create"),
    path("product_detail/<int:product_id>", product_detail, name="product_detail")
]
