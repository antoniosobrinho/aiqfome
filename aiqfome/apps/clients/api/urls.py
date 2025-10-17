from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.clients.api.views.client_viewset import ClientViewSet

router = DefaultRouter()

router.register(r"", ClientViewSet, basename="clients")

urlpatterns = [
    path("", include(router.urls)),
]
