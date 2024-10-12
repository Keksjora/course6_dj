from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (AddProductView, CatalogContactsView, CatalogDetailView,
                    CatalogHomeView, ProductDeleteView)

app_name = "catalog"

urlpatterns = [
    path("home/", CatalogHomeView.as_view(), name="home"),
    path("contacts/", CatalogContactsView.as_view(), name="contacts"),
    path("product/<int:pk>/", CatalogDetailView.as_view(), name="product_info"),
    path("add_product/", AddProductView.as_view(), name="add_product"),
    path(
        "product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
