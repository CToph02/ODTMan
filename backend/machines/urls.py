from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MachineViewSet, MachineModelViewSet, MachineBrandViewSet, MachineCategoryViewSet

router = DefaultRouter()
router.register(r'units', MachineViewSet)
router.register(r'models', MachineModelViewSet)
router.register(r'brands', MachineBrandViewSet)
router.register(r'categories', MachineCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]