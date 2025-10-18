from django.urls import include, path
from rest_framework_nested import routers

from apps.clients.api.viewsets.client_favorite_product_viewset import (
    ClientFavoriteProductViewSet,
)
from apps.clients.api.viewsets.client_viewset import ClientViewSet

router = routers.DefaultRouter()

router.register(r"", ClientViewSet, basename="clients")

client_router = routers.NestedDefaultRouter(router, r"", lookup="client")
client_router.register(
    r"favorite_products",
    ClientFavoriteProductViewSet,
    basename="client-favorite-products",
)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(client_router.urls)),
]
