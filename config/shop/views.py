from django.shortcuts import render
from .models import Product, Order

def index(request):
    return render(request, "shop/index.html")

def catalog(request):
    product_list = Product.objects.all()
    return render(request, "shop/catalog.html", {"products":product_list})

def orders(request):
    orderss = Order.objects.all()
    return render(request, "shop/orders.html", {"orders":orderss})

def order_create(request):
    return render(request, "shop/order_create.html")

def product_detail(request, product_id):
    product_in_bd = Product.objects.get(id=product_id)
    return render(request, "shop/product_detail.html", {"product": product_in_bd})

