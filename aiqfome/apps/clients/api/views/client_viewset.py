from rest_framework import viewsets

from apps.clients.api.serializers.client_serializer import ClientSerializer
from apps.clients.models import Client


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
