from rest_framework.response import Response
from rest_framework import status, viewsets
from apps.products.api.serializers.product_serializer import ProductSerializer
from apps.products.services.product_service import ProductService


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        product_service = ProductService()
        products = product_service.get_products()

        products_serializer = ProductSerializer(products, many=True)

        return Response(products_serializer.data, status.HTTP_200_OK)
