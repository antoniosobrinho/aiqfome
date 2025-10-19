from rest_framework import serializers

from apps.clients.models import ClientFavoriteProduct


class ClientFavoriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientFavoriteProduct
        fields = "__all__"


class CreateClientFavoriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientFavoriteProduct
        fields = ["client", "product_id"]
