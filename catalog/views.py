from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Category, Product


def home(request):

    latest_products = Product.objects.order_by("created_at")[:5]

    for product in latest_products:
        print(f"Product: {product.name}, Price: {product.price}")
    return render(request, "catalog/home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
    return render(request, "catalog/contacts.html")
