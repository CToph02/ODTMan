from rest_framework import viewsets
from .serializers import ClientSerializer
from .models import Client
from odtman.mixins import MessageResponseMixin

class ClientViewSet(MessageResponseMixin, viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    verbose_name = "The client"