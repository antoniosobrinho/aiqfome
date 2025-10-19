from rest_framework import viewsets, status, mixins

from apps.clients.api.serializers.client_favorite_product_serializer import (
    ClientFavoriteProductSerializer,
    CreateClientFavoriteProductSerializer,
)
from apps.clients.models import ClientFavoriteProduct
from apps.clients.services.client_favorite_product_service import (
    ClientFavoriteProductService,
)
from apps.products.exceptions import ProductNotFoundError
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class ClientFavoriteProductViewSet(
    viewsets.ReadOnlyModelViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin
):

    def get_serializer_class(self):
        if self.action == "create":
            return CreateClientFavoriteProductSerializer

        return ClientFavoriteProductSerializer

    def get_queryset(self):
        client_id = self.kwargs.get("client_pk")
        return ClientFavoriteProduct.objects.filter(client_id=client_id)

    def create(self, request, *args, **kwargs):
        data = request.data
        data["client"] = self.kwargs.get("client_pk")

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        serialized_data = serializer.validated_data

        try:
            service = ClientFavoriteProductService()
            favorite_product = service.create(
                serialized_data["client"], serialized_data["product_id"]
            )
        except ProductNotFoundError as error:
            raise ValidationError({"product_id": "Produto não encontrado"})

        serializer = ClientFavoriteProductSerializer(favorite_product)

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
