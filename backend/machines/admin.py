from django.contrib import admin
from .models import Machine, MachineBrand, MachineCategory, MachineModel
# Register your models here.

admin.site.register(MachineModel)
admin.site.register(MachineCategory)
admin.site.register(MachineBrand)
admin.site.register(Machine)
