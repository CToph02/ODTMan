from rest_framework import viewsets, status
from rest_framework.response import Response
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
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(
            {'message': 'La marca ha sido eliminada correctamente'},
            status=status.HTTP_200_OK
        )
class MachineCategoryViewSet(viewsets.ModelViewSet):
    queryset = MachineCategory.objects.all()
    serializer_class = MachineCategorySerializer
    