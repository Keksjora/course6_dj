from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from .views import (
    AddProductView,
    CatalogContactsView,
    CatalogDetailView,
    CatalogHomeView,
    CategoryListView,
    ProductDeleteView,
    ProductsByCategoryView,
    ProductUpdateView,
)

app_name = "catalog"

urlpatterns = [
    path("", CatalogHomeView.as_view(), name="home"),
    path("contacts/", CatalogContactsView.as_view(), name="contacts"),
    path(
        "product/<int:pk>/",
        cache_page(60)(CatalogDetailView.as_view()),
        name="product_info",
    ),
    path("add_product/", AddProductView.as_view(), name="add_product"),
    path(
        "product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
    path(
        "category/<int:category_id>/products/",
        ProductsByCategoryView.as_view(),
        name="category_products",
    ),
    path("category_list/", CategoryListView.as_view(), name="category_list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
