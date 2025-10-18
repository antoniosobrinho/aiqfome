from typing import List, Optional
from django.conf import settings
from rest_framework import status
import requests


class ProductService:
    def get_products(self) -> List:
        try:
            response = requests.get(settings.PRODUCTS_API)
            if response.status_code == status.HTTP_200_OK:
                return response.json()
            return []
        except:
            return []

    def get_product_by_id(self, product_id: int) -> Optional[dict]:
        try:
            response = requests.get(settings.PRODUCTS_API + f"/{product_id}")
            if response.status_code == status.HTTP_200_OK:
                return response.json()
            return None
        except:
            return None
