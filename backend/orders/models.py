from django.db import models
from django.conf import settings
from clients.models import Client
from machines.models import Machine
from odtman.model_base import TimeStampedModel

class RepairStatus(models.Model):
    status = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.status}'

class PaymentMethod(models.Model):
    method = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.method}'

class OdtOrders(TimeStampedModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_orders')
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='machine_orders')
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, related_name='payment_method_orders')
    repair_status = models.ForeignKey(RepairStatus, on_delete=models.CASCADE, related_name='repair_status_orders')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_by_orders')
    technician = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='technician_orders', null=True, blank=True)

    total_payment = models.DecimalField(decimal_places=2, max_digits=15)
    client_description = models.TextField()
    diagnostic = models.TextField()

    def __str__(self):
        return f'{self.machine} - {self.client}'
