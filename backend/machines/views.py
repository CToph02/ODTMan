from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import MachineSerializer, MachineModelSerializer, MachineCategorySerializer, MachineBrandSerializer
from .models import Machine, MachineBrand, MachineCategory, MachineModel
from odtman.mixins import MessageResponseMixin

class MachineViewSet(MessageResponseMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    verbose_name = "The machine"

class MachineModelViewSet(MessageResponseMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MachineModel.objects.all()
    serializer_class = MachineModelSerializer
    verbose_name = "The model"

class MachineBrandViewSet(MessageResponseMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = MachineBrandSerializer
    queryset = MachineBrand.objects.all()
    verbose_name = "The brand"
    
class MachineCategoryViewSet(MessageResponseMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = MachineCategory.objects.all()
    serializer_class = MachineCategorySerializer
    verbose_name = "The category"
    