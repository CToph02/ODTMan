from rest_framework import viewsets
from .serializers import MachineSerializer, MachineModelSerializer, MachineCategorySerializer, MachineBrandSerializer
from .models import Machine, MachineBrand, MachineCategory, MachineModel

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class MachineModelViewSet(viewsets.ModelViewSet):
    queryset = MachineModel.objects.all()
    serializer_class = MachineModelSerializer

class MachineBrandViewSet(viewsets.ModelViewSet):
    serializer_class = MachineBrandSerializer

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return MachineBrand.objects.none()
        return MachineBrand.objects.all()

class MachineCategoryViewSet(viewsets.ModelViewSet):
    queryset = MachineCategory.objects.all()
    serializer_class = MachineCategorySerializer
    