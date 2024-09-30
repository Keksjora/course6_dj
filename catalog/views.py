from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView

from catalog.models import Product

from .forms import ProductForm


class CatalogHomeView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"


class CatalogContactsView(View):
    def get(self, request):
        return render(request, "catalog/contacts.html")

    def post(self, request):
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(f'Спасибо, {name}! Сообщение "{message}" получено.')


class CatalogDetailView(DetailView):
    model = Product
    template_name = "catalog/product_info.html"
    context_object_name = "product"


class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/add_product.html"
    success_url = reverse_lazy("catalog:home")
