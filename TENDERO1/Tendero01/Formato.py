from django import forms
from .models import *



class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = '__all__'
        labels = {
            'Emp_cargo_id': 'Cargo',

        }
class ProvedoresForm(forms.ModelForm):
    class Meta:
        model = proveedores
        fields = '__all__'


class ProductosForm(forms.ModelForm):
    class Meta:
        model = productos
        fields = '__all__'
        labels = {
            'Prod_categoria':'Categoría',
            'Prod_provedor':'Proveedor'
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = categoria_pro
        fields = '__all__'


class ClienteForm(forms.ModelForm):
    class Meta:
        model = clientes
        fields = '__all__'


class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'
        labels = {
            'Usu_emp_id': 'Empleado',
            'Usu_cargo_id': 'Cargo'
        }

class Factura_DetalleForm(forms.ModelForm):
    class Meta:
        model = Detalle_fac
        fields = '__all__'
        labels = {
            'Det_id_cli': 'Cliente',
            'Det_fac_id': 'Factura'
        }

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago_empleado
        fields = '__all__'
        labels = {
            'Pagemple_empl_id': 'Empleado',
            'Pagemple_carg_id': 'Cargo'
        }

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = '__all__'
        labels = {
            'Fac_prod': 'Producto',
        }