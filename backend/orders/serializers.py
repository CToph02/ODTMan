from rest_framework import serializers
from .models import OdtOrders, PaymentMethod, RepairStatus

class OdtOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OdtOrders
        fields = '__all__'

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['id', 'method']

class RepairStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairStatus
        fields = ['id', 'status']