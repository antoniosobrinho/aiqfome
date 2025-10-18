from rest_framework import viewsets, status

from apps.clients.api.serializers.client_favorite_product_serializer import (
    ClientFavoriteProductSerializer,
)
from apps.clients.models import ClientFavoriteProduct
from rest_framework.response import Response


class ClientFavoriteProductViewSet(viewsets.ModelViewSet):
    serializer_class = ClientFavoriteProductSerializer

    def get_queryset(self):
        client_id = self.kwargs.get("client_pk")
        return ClientFavoriteProduct.objects.filter(client_id=client_id)

    def create(self, request, *args, **kwargs):
        data = request.data
        data["client"] = self.kwargs.get("client_pk")

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
