from rest_framework import serializers

from apps.clients.api.validators.product_validators import ProductValidator
from apps.clients.models import ClientFavoriteProduct


class ClientFavoriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientFavoriteProduct
        fields = "__all__"

    def validate_product(self, value):
        product_validators = ProductValidator()
        product_validators.validate_product_exists(value)

        return value
