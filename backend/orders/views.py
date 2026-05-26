from rest_framework import viewsets
from .serializers import OdtOrdersSerializer, PaymentMethodSerializer, RepairStatusSerializer
from .models import OdtOrders, PaymentMethod, RepairStatus
from odtman.mixins import MessageResponseMixin

class OdtOrdersViewSet(MessageResponseMixin, viewsets.ModelViewSet):
    queryset = OdtOrders.objects.all()
    serializer_class = OdtOrdersSerializer
    verbose_name = "The order"

class PaymentMethodViewSet(MessageResponseMixin, viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    verbose_name = "The payment"

class RepairStatusViewSet(MessageResponseMixin, viewsets.ModelViewSet):
    queryset = RepairStatus.objects.all()
    serializer_class = RepairStatusSerializer
    verbose_name = "The repair status"