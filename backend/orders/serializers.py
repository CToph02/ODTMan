from rest_framework import serializers
from clients.serializers import ClientSerializer
from machines.serializers import MachineSerializer
from user_auth.serializers import UserSerializer
from .models import OdtOrders, PaymentMethod, RepairStatus

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['id', 'method']

class RepairStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairStatus
        fields = ['id', 'status']

class OdtOrdersSerializer(serializers.ModelSerializer):
    client_details = ClientSerializer(source='client', read_only=True)
    machine_details = MachineSerializer(source='machine', read_only=True)
    payment_method_details = PaymentMethodSerializer(source='payment_method', read_only=True)
    repair_status_details = RepairStatusSerializer(source='repair_status',read_only=True)
    created_by_details = UserSerializer(source='created_by', read_only=True)
    technician_details = UserSerializer(source='technician', read_only=True)
    class Meta:
        model = OdtOrders
        fields = [
            'id',
            'client_details',
            'machine_details', 
            'payment_method_details',
            'repair_status_details',
            'created_by_details',
            'technician_details',
            'total_payment',
            'client_description',
            'diagnostic',
            'created_at',
            'updated_at'
        ]