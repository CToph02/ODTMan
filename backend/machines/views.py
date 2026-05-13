from rest_framework import viewsets
from rest_framework import serializers
from .serializers import MachineSerializer, MachineModelSerializer
from .models import Machine, MachineBrand, MachineCategory, MachineModel

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class MachineModelViewSet(viewsets.ModelViewSet):
    queryset = MachineModel.objects.all()
    serializer_class = MachineModelSerializer

class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MachineBrand.objects.all()
    serializer_class = serializers.ModelSerializer

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MachineCategory.objects.all()
    serializer_class = serializers.ModelSerializer
    