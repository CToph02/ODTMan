from django.core.validators import RegexValidator
from rest_framework import serializers
from .models import Machine, MachineBrand, MachineCategory, MachineModel

class MachineSerializer(serializers.ModelSerializer):
    serial_number = serializers.CharField(
        validators=[
            RegexValidator(
                regex = r"""^[^@'$"´`]+$""",
                message="El número serial no puede contener catacteres especiales."
            )
        ]
    )
    class Meta:
        model = Machine
        fields = ['id', 'model', 'serial_number']

class MachineBrandSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(
        validators=[
            RegexValidator(
                regex = '^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9\\s-]+$',
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
        extra_kwargs = {
            'category':{
                'validators': [
                    RegexValidator(
                        regex = '^[A-Za-zÁÉÍÓÚáéíóúÑñ0-9\\s]+$',
                        message="La categoría solo puede contener letras, números y espacios."
                    )
                ],
                'error_messages': {
                    'unique': 'La categoría ya existe.'
                }
            }
        }

class MachineModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineModel
        fields = ['id', 'model', 'brand', 'category']
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if instance.brand:
            representation['brand'] = MachineBrandSerializer(instance.brand).data
        if instance.category:
            representation['category'] = MachineCategorySerializer(instance.category).data
        return representation
