from django.db import models

class MachineBrand(models.Model):
    brand = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.brand}'

class MachineCategory(models.Model):
    category = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return f'{self.category}'

class MachineModel(models.Model):
    model = models.CharField(max_length=100)
    category = models.ForeignKey(MachineCategory, on_delete=models.CASCADE, related_name='category_models')
    brand = models.ForeignKey(MachineBrand, on_delete=models.CASCADE, related_name='brand_models')
    
    def __str__(self):
        return f'{self.model} {self.brand}'

class Machine(models.Model):
    serial_number = models.CharField(max_length=200)
    model = models.ForeignKey(MachineModel, on_delete=models.CASCADE, related_name='machines')
    
    def __str__(self):
        return f'{self.model} - ({self.serial_number})'