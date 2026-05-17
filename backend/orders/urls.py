from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OdtOrdersViewSet, RepairStatusViewSet, PaymentMethodViewSet

router = DefaultRouter()
router.register(r'odt', OdtOrdersViewSet)
router.register(r'status', RepairStatusViewSet)
router.register(r'payment', PaymentMethodViewSet)

urlpatterns = [
    path('', include(router.urls)),
]