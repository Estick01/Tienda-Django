from django.urls import path
from django.contrib.auth.decorators import login_required
from TENDERO1.Tendero01.views import Empleado,crearEmpleado,editarEmpleado,eliminarEmpleado,Productos,editarproducto,crearProducto,eliminarproducto,Proveedores,crearProveedor,eliminarProveedor,editarProveedor,cargo,crearCargo,editarCargo,eliminarCargo,categoria,crearCategoria,editarCategoria,eliminarCategoria,\
    Clientes,crearCliente,editarClientes,eliminarCliente,usuario,crearUsuario,editarUsuario,eliminarUsuario,Factura_detalle,crearFactura_Detalle,editarFactura_Detalle,eliminarFactura_Detalle,pago,crearPago,editarPago,eliminarPago,factura,crearFactura,editarFactura,eliminarFactura
urlpatterns = [

    path('mostrarEmpleado/',login_required(Empleado),name='mostrarEmpleados'),
    path('crearEmpleado/',login_required(crearEmpleado.as_view()),name='crearEmpleado'),
    path('editarEmpleado/<int:pk>/',login_required(editarEmpleado.as_view()),name='editarEmpleado'),
    path('eliminarEmpleado/<int:pk>/',login_required(eliminarEmpleado.as_view()),name='elimnarEmpleado'),

    path('mostrarProducto/',login_required(Productos), name='mostrarProducto'),
    path('crearProducto/',login_required(crearProducto.as_view()),name='crearProducto'),
    path('editarProducto/<int:pk>/',login_required(editarproducto.as_view()),name='editarProducto'),
    path('eliminarproducto/<int:pk>/',login_required(eliminarproducto.as_view()),name='elimnarProducto'),

    path('mostrarProveedor/',login_required(Proveedores), name='mostrarProveedor'),
    path('crearProveedor/',login_required(crearProveedor.as_view()), name='crearProveedor'),
    path('editarProveedor/<int:pk>/', login_required(editarProveedor.as_view()), name='editarProveedor'),
    path('eliminarProveedor/<int:pk>/',login_required(eliminarProveedor.as_view()), name='elimnarProveedor'),

    path('mostrarCargo/',login_required(cargo), name='mostrarCargo'),
    path('crearCargo/',login_required(crearCargo.as_view()), name='crearCargo'),
    path('editarCargo/<int:pk>/',login_required(editarCargo.as_view()), name='editarCargo'),
    path('eliminarCargo/<int:pk>/',login_required(eliminarCargo.as_view()), name='elimnarCargo'),

    path('mostrarCategoria/',login_required(categoria), name='mostrarCategoria'),
    path('crearCategoria/',login_required(crearCategoria.as_view()), name='crearCategoria'),
    path('editarCategoria/<int:pk>/',login_required(editarCategoria.as_view()), name='editarCategoria'),
    path('eliminarCategoria/<int:pk>/',login_required(eliminarCategoria.as_view()), name='elimnarCategoria'),

    path('mostrarClientes/',login_required(Clientes), name='mostrarClienetes'),
    path('crearCliente/', login_required(crearCliente.as_view()), name='crearCliente'),
    path('editarCliente/<int:pk>/',login_required(editarClientes.as_view()), name='editarCliente'),
    path('eliminarCliente/<int:pk>/',login_required(eliminarCliente.as_view()), name='elimnarCliente'),

    path('mostrarUsuario/',login_required(usuario), name='mostrarUsuario'),
    path('crearUsuario/', login_required(crearUsuario.as_view()), name='crearUsuario'),
    path('editarUsuario/<int:pk>/',login_required(editarUsuario.as_view()), name='editarUsuaio'),
    path('eliminarUsuario/<int:pk>/',login_required(eliminarUsuario.as_view()), name='elimnarUsuario'),

    path('mostrarFactura_detalle/',login_required(Factura_detalle.as_view()), name='mostrarFactura_Detalle'),
    path('creaFactura_detalle/',login_required(crearFactura_Detalle.as_view()), name='crearFactura_Detalle'),
    path('editarFactura_detalle/<int:pk>/',login_required(editarFactura_Detalle.as_view()), name='editarFactura_Detalle'),
    path('eliminarFactura_detalle/<int:pk>/',login_required(eliminarFactura_Detalle.as_view()), name='elimnarFactura_Detalle'),

    path('mostrarPago/',login_required(pago), name='mostrarPago'),
    path('crearPago/',login_required(crearPago.as_view()), name='crearPago'),
    path('editarPago/<int:pk>/',login_required(editarPago.as_view()), name='editarPago'),
    path('eliminarPago/<int:pk>/',login_required(eliminarPago.as_view()), name='elimnarPago'),

    path('mostrarFactura/',login_required(factura), name='mostrarFactura'),
    path('crearFactura/',login_required(crearFactura.as_view()), name='crearFactura'),
    path('editarFactura/<int:pk>/',login_required(editarFactura.as_view()), name='editarFactura'),
    path('eliminarFactura/<int:pk>/',login_required(eliminarFactura.as_view()), name='elimnarFactura'),
]