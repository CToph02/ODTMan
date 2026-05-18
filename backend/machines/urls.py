from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MachineViewSet, MachineModelViewSet, MachineBrandViewSet, MachineCategoryViewSet

router = DefaultRouter()
router.register(r'units', MachineViewSet, basename='machine')
router.register(r'models', MachineModelViewSet, basename='machine_model')
router.register(r'brands', MachineBrandViewSet, basename='machine_brand')
router.register(r'categories', MachineCategoryViewSet, basename='machine_category')

urlpatterns = [
    path('', include(router.urls)),
]