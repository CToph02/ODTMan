from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OdtOrdersSerializer, PaymentMethodSerializer, RepairStatusSerializer
from .models import OdtOrders, PaymentMethod, RepairStatus

class OdtOrdersViewSet(viewsets.ModelViewSet):
    queryset = OdtOrders.objects.all()
    serializer_class = OdtOrdersSerializer

class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

class RepairStatusViewSet(viewsets.ModelViewSet):
    queryset = RepairStatus.objects.all()
    serializer_class = RepairStatusSerializer