from django.db import models


# Create your models here.
class Client(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)


class ClientFavoriteProduct(models.Model):
    class Meta:
        unique_together = ("client", "product_id")

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product_id = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    price = models.FloatField()
