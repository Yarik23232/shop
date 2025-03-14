from django.shortcuts import render
from .models import Product, Order

def catalog(request):
    product_list = Product.objects.all()
    return render(request, "shop/catalog.html", {"products":product_list})

def orders(request):
    orderss = Order.objects.all()
    return render(request, "shop/orders.html", {"orders":orderss})

def order_create(request):
    return render(request, "shop/order_create.html")