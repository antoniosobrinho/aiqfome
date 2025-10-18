from apps.products.services.product_service import ProductService
from rest_framework.exceptions import ValidationError


class ProductValidator:
    def validate_product_exists(self, product_id: int):
        product_service = ProductService()

        product = product_service.get_product_by_id(product_id)

        if not product:
            raise ValidationError("Produto não existe.")
