from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MachineViewSet, MachineModelViewSet

router = DefaultRouter()
router.register(r'units', MachineViewSet)
router.register(r'models', MachineModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]