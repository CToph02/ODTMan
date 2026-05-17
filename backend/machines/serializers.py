from django.core.validators import RegexValidator
from rest_framework import serializers
from .models import Machine, MachineBrand, MachineCategory, MachineModel

class MachineModelSerializer(serializers.ModelSerializer):
    brand_name = serializers.ReadOnlyField(source='brand.brand')
    category_name = serializers.ReadOnlyField(source='category.category')

    class Meta:
        model = MachineModel
        fields = ['id', 'model', 'brand', 'category', 'brand_name', 'category_name']

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = ['id', 'model', 'serial_number']

class MachineBrandSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(
        validators=[
            RegexValidator(
                regex = '^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9\s]+$',
                message="La marca solo puede contener letras, números y espacios."
            )
        ]
    )

    class Meta:
        model = MachineBrand
        fields = ['id', 'brand']

class MachineCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineCategory
        fields = ['id', 'category']