from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from catalog.models import Product

from .forms import ProductForm, ProductModeratorForm


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


class AddProductView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/add_product.html"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog/product_delete.html"
    success_url = reverse_lazy("catalog:home")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("product.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/add_product.html"
    success_url = reverse_lazy("catalog:home")
