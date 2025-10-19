from apps.clients.models import Client, ClientFavoriteProduct
from apps.products.exceptions import ProductNotFoundError
from apps.products.services.product_service import ProductService


class ClientFavoriteProductService:
    def create(self, client: Client, product_id: int) -> ClientFavoriteProduct:
        product = self.get_product_by_id(product_id)

        favorite_product = ClientFavoriteProduct.objects.create(
            client=client,
            product_id=product.get("id"),
            title=product.get("title"),
            image=product.get("image"),
            price=product.get("price"),
        )

        return favorite_product

    def get_product_by_id(self, product_id: int):
        product_service = ProductService()
        product = product_service.get_product_by_id(product_id)

        if not product:
            raise ProductNotFoundError()

        return product
