from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.products.api.viewsets.product_viewset import ProductViewSet

router = DefaultRouter()

router.register(r"", ProductViewSet, basename="products")

urlpatterns = [
    path("", include(router.urls)),
]
