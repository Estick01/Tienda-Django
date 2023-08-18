
from django.shortcuts import render
from .models import Empleados
from django.views.generic import CreateView,DeleteView,ListView,UpdateView,TemplateView,View
from django.urls import reverse_lazy
from .Formato import *
from django.db.models import Q
from django.core.paginator import Paginator



class Inicio(View):
    def get(self,request,*args,**kwargs):
        return render(request,'inicio/index.html')


def Empleado(request):
    busqueda = request.GET.get("buscar")
    Emplead = Empleados.objects.all()
    if busqueda:
        Emplead = Empleados.objects.filter(
            Q(Emp_nombre__icontains= busqueda) |
            Q(Emp_apellido__icontains = busqueda) |
            Q(Emp_direccion__icontains = busqueda)|
            Q(Emp_cedula__icontains=busqueda) |
            Q(Emp_telefono__icontains=busqueda) |
            Q(Emp_cargo_id__Carg_descrip__icontains=busqueda) |
            Q(Emp_cargo_id__Carg_salario__icontains=busqueda)
        ).distinct()
    paginator = Paginator(Emplead,5)
    page = request.GET.get('page')
    Emplead = paginator.get_page(page)

    return render(request, 'Cobrador/Empleado.html', {'Empleado':Emplead})

class crearEmpleado(CreateView):
    model = Empleados
    form_class = EmpleadoForm
    template_name = 'Cobrador/Crear_Cobrador.html'
    success_url = reverse_lazy('tendero:mostrarEmpleados')

class editarEmpleado(UpdateView):
    model = Empleados
    form_class = EmpleadoForm
    template_name = 'Cobrador/Editar_empleado.html'
    success_url = reverse_lazy('tendero:mostrarEmpleados')

class eliminarEmpleado(DeleteView):
    model = Empleados
    template_name = 'Cobrador/Verificacion_Empleado.html'
    success_url = reverse_lazy('tendero:mostrarEmpleados')


def Productos(request):
    busqueda = request.GET.get("buscar")
    Prod = productos.objects.all()
    if busqueda:
        Prod = productos.objects.filter(
            Q(Prod_nombre__icontains = busqueda) |
            Q(Prod_embalaje__icontains = busqueda) |
            Q(Prod_categoria__Cate_nombre__icontains =busqueda) |
            Q(Prod_provedor__Prov_nombre__icontains=busqueda)
        ).distinct()
    paginator = Paginator(Prod,2)
    page = request.GET.get('page')
    Prod = paginator.get_page(page)
    return render(request,'Producto/Productos.html', {'producto':Prod})

class crearProducto(CreateView):
    model = productos
    form_class = ProductosForm
    template_name = 'Producto/Crear_Producto.html'
    success_url = reverse_lazy('tendero:mostrarProducto')
class editarproducto(UpdateView):
    model = productos
    form_class = ProductosForm
    template_name = 'Producto/Editar_producto.html'
    success_url = reverse_lazy('tendero:mostrarProducto')
class eliminarproducto(DeleteView):
    model = productos
    template_name = 'Producto/Verificacion_Producto.html'
    success_url = reverse_lazy('tendero:mostrarProducto')





def Proveedores(request):
    busqueda = request.GET.get("buscar")
    Prov = proveedores.objects.all()
    if busqueda:
        Prov = proveedores.objects.filter(
            Q(Prov_nombre__icontains = busqueda) |
            Q(Prov_replegal__icontains =busqueda) |
            Q(Prov_nit__icontains=busqueda) |
            Q(Prov_telefono__icontains=busqueda) |
            Q(Prov_ciudad__icontains=busqueda)
        ).distinct()
    paginator = Paginator(Prov,2)
    page = request.GET.get('page')
    Prov = paginator.get_page(page)
    return render(request,'Proveedor/Proveedor.html', {'proveedor':Prov})

class crearProveedor(CreateView):
    model = proveedores
    form_class = ProvedoresForm
    template_name = 'Proveedor/Crear_Proveedor.html'
    success_url = reverse_lazy('tendero:mostrarProveedor')
class editarProveedor(UpdateView):
    model = proveedores
    form_class = ProvedoresForm
    template_name = 'Proveedor/Editar_proveedore.html'
    success_url = reverse_lazy('tendero:mostrarProveedor')
class eliminarProveedor(DeleteView):
    model = proveedores
    template_name = 'Proveedor/Verificacion_Proveedor.html'
    success_url = reverse_lazy('tendero:mostrarProveedor')



def cargo(request):
    busqueda = request.GET.get("buscar")
    cargo = Cargo.objects.all()
    if busqueda:
        cargo = Cargo.objects.filter(
            Q(Carg_descrip__icontains = busqueda) |
            Q(Carg_salario__icontains = busqueda)

        ).distinct()
    paginator = Paginator(cargo,2)
    page = request.GET.get('page')
    cargo = paginator.get_page(page)

    return render(request,'Cargo/Cargo.html', {'Cargo':cargo})

class crearCargo(CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'Cargo/Crear_Cargo.html'
    success_url = reverse_lazy('tendero:mostrarCargo')
class editarCargo(UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'Cargo/Editar_cargo.html'
    success_url = reverse_lazy('tendero:mostrarCargo')
class eliminarCargo(DeleteView):
    model = Cargo
    template_name = 'Cargo/Verificacion_Cargo.html'
    success_url = reverse_lazy('tendero:mostrarCargo')


def categoria(request):
    busqueda = request.GET.get("buscar")
    Categoria = categoria_pro.objects.all()
    if busqueda:
        Categoria = categoria_pro.objects.filter(
            Q(Cate_nombre__icontains = busqueda) |
            Q(Cate_descripcion__icontains =busqueda)
        ).distinct()
    paginator = Paginator(Categoria,2)
    page = request.GET.get('page')
    Categoria = paginator.get_page(page)
    return render(request,'Categoria/Categoria.html', {'Categoria':Categoria})

class crearCategoria(CreateView):
    model = categoria_pro
    form_class = CategoriaForm
    template_name = 'Categoria/Crear_Categoria.html'
    success_url = reverse_lazy('tendero:mostrarCategoria')
class editarCategoria(UpdateView):
    model = categoria_pro
    form_class = CategoriaForm
    template_name = 'Categoria/Editar_categoria.html'
    success_url = reverse_lazy('tendero:mostrarCategoria')
class eliminarCategoria(DeleteView):
    model = categoria_pro
    template_name = 'Categoria/Verificacion_Categoria.html'
    success_url = reverse_lazy('tendero:mostrarCategoria')



def Clientes(request):
    busqueda = request.GET.get("buscar")
    clien = clientes.objects.all()
    if busqueda:
        clien = clientes.objects.filter(
            Q(Cli_nombre__icontains = busqueda) |
            Q(Cli_apellido__icontains =busqueda) |
            Q(Cli_cedula__icontains=busqueda) |
            Q(Cli_ciudad__icontains=busqueda) |
            Q(Cli_telefono__icontains=busqueda) |
            Q(Cli_direccion__icontains=busqueda)
        ).distinct()
    paginator = Paginator(clien,2)
    page = request.GET.get('page')
    clien = paginator.get_page(page)

    return render(request,'Clientes/Cliente.html', {'Cliente':clien })

class crearCliente(CreateView):
    model = clientes
    form_class = ClienteForm
    template_name = 'Clientes/Crear_Cliente.html'
    success_url = reverse_lazy('tendero:mostrarClienetes')
class editarClientes(UpdateView):
    model = clientes
    form_class = ClienteForm
    template_name = 'Clientes/Editar_cliente.html'
    success_url = reverse_lazy('tendero:mostrarClienetes')
class eliminarCliente(DeleteView):
    model = clientes
    template_name = 'Clientes/Verificacion_Cliente.html'
    success_url = reverse_lazy('tendero:mostrarClienetes')



def usuario(request):
    busqueda = request.GET.get("buscar")
    user = Usuarios.objects.all()
    if busqueda:
        user = Usuarios.objects.filter(
            Q(Usu_nombre__icontains = busqueda) |
            Q(Usu_password_icontains =busqueda) |
            Q(Usu_cargo_id__Carg_descrip__icontains=busqueda)
        ).distinct()
    paginator = Paginator(user,2)
    page = request.GET.get('page')
    user = paginator.get_page(page)
    return render(request,'Usuario/Usuario.html', {'usuario':user })

class crearUsuario(CreateView):
    model = Usuarios
    form_class = UsuarioForm
    template_name = 'Usuario/Crear_Usuario.html'
    success_url = reverse_lazy('tendero:mostrarUsuario')
class editarUsuario(UpdateView):
    model = Usuarios
    form_class = UsuarioForm
    template_name = 'Usuario/Editar_usuario.html'
    success_url = reverse_lazy('tendero:mostrarUsuario')
class eliminarUsuario(DeleteView):
    model = Usuarios
    template_name = 'Usuario/Verificacion_Usuario.html'
    success_url = reverse_lazy('tendero:mostrarUsuario')



class Factura_detalle(ListView):
    model = Detalle_fac
    template_name = 'Detalle_Factura/Detalle_factura.html'
class crearFactura_Detalle(CreateView):
    model = Detalle_fac
    form_class = Factura_DetalleForm
    template_name = 'Detalle_Factura/Crear_Detalle_factura.html'
    success_url = reverse_lazy('tendero:mostrarFactura_Detalle')
class editarFactura_Detalle(UpdateView):
    model = Detalle_fac
    form_class = Factura_DetalleForm
    template_name = 'Detalle_Factura/Crear_Detalle_factura.html'
    success_url = reverse_lazy('tendero:mostrarFactura_Detalle')
class eliminarFactura_Detalle(DeleteView):
    model = Detalle_fac
    template_name = 'Detalle_Factura/Verificacion_Detalle_Factura.html'
    success_url = reverse_lazy('tendero:mostrarFactura_Detalle')

def pago(request):
    busqueda = request.GET.get("buscar")
    pago = Pago_empleado.objects.all()
    if busqueda:
        pago = Pago_empleado.objects.filter(
            Q(Pagemple_empl_id__Emp_nombre__icontains = busqueda) |
            Q(Pagemple_empl_id__Emp_apellido__icontains=busqueda) |
            Q(Pagemple_carg_id__Carg_descrip__icontains =busqueda)

        ).distinct()
    paginator = Paginator(pago,2)
    page = request.GET.get('page')
    pago = paginator.get_page(page)
    return render(request,'Pago_Empleado/Pago.html', {'pago':pago })
class crearPago(CreateView):
    model = Pago_empleado
    form_class = PagoForm
    template_name = 'Pago_Empleado/Crear_Pago_Empleado.html'
    success_url = reverse_lazy('tendero:mostrarPago')
class editarPago(UpdateView):
    model = Pago_empleado
    form_class = PagoForm
    template_name = 'Pago_Empleado/Editar_pago_empleado.html'
    success_url = reverse_lazy('tendero:mostrarPago')
class eliminarPago(DeleteView):
    model = Pago_empleado
    template_name = 'Pago_Empleado/Verificacion_Pago_Empleado.html'
    success_url = reverse_lazy('tendero:mostrarPago')


def factura(request):
    busqueda = request.GET.get("buscar")
    fact = Factura.objects.all()
    if busqueda:
        fact = Factura.objects.filter(
            Q(Usu_nombre__icontains = busqueda) |
            Q(Usu_password_icontains =busqueda) |
            Q(Usu_cargo_id__Carg_descrip__icontains=busqueda)
        ).distinct()
    paginator = Paginator(fact,2)
    page = request.GET.get('page')
    fact = paginator.get_page(page)
    return render(request,'Factura/Factura.html', {'factura':fact })

class crearFactura(CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'Factura/Crear_Factura.html'
    success_url = reverse_lazy('tendero:mostrarFactura')
class editarFactura(UpdateView):
    model = Factura
    form_class = FacturaForm
    template_name = 'Factura/Editar_factura.html'
    success_url = reverse_lazy('tendero:mostrarFactura')
class eliminarFactura(DeleteView):
    model = Factura
    template_name = 'Factura/Verificacion_Factura.html'
    success_url = reverse_lazy('tendero:mostrarFactura')