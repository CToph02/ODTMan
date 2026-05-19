from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from user_auth.models import CustomUser

from .models import MachineBrand, MachineCategory, MachineModel

# Create your tests here.
class VistaProtegida(APITestCase):
    def setUp(self):
        self.user, created = CustomUser.objects.get_or_create(username="Esteban")

        if created:
            self.user.set_password("1234")
            self.user.save()

        credenciales = {
            "username":self.user.username,
            "password":"1234"
        }
        login_url = reverse("login")
        response = self.client.post(login_url, credenciales, format="json")
        self.access_token = response.data["access"]
        
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")
        self.url_brand = reverse("machine_brand-list")
        self.url_category = reverse("machine_category-list")
        self.url_model = reverse("machine_model-list")
        self.url_machine = reverse("machine-list")

    def test_create_brand(self):
        data = {"brand": "Epson"}
        response = self.client.post(self.url_brand, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_category(self):
        data = {"category": "Impresora"}
        response = self.client.post(self.url_category, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_model(self):
        brand = MachineBrand.objects.create(brand="Epson")
        category = MachineCategory.objects.create(category="Impresora")
        data = {
            "brand": brand.id,            
            "category": category.id,
            "model": "L3210"
        }
        response = self.client.post(self.url_category, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_machine(self):
        brand = MachineBrand.objects.create(brand="Epson")
        category = MachineCategory.objects.create(category="Impresora")
        model = MachineModel.objects.create(model="L3210", brand=brand, category=category)
        data = {
            "model": model.id,
            "serial_number": "8273jdj87"
        }
        response = self.client.post(self.url_machine, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)