from django.contrib import admin
from .models import Empleados
from .models import Cargo

admin.site.register(Empleados)
admin.site.register(Cargo)