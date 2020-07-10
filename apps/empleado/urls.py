from django.urls import path
from . import views

app_name = 'empleado'
# Las URL del empleado aca

urlpatterns = [
    path('empleado/', views.home_empleado, name='base_empleado.html'),
    path('empleado/gestionclientes/', views.ClienteCreate, name="gestion_cliente.html"),
    path('empleado/listado-clientes/', views.ClienteList, name="listado_cliente.html"),
    path('empleado/huespedes/', views.HuespedesList, name='huespedes.html'),
    path('empleado/gestion-productos/', views.ProductoCreate, name='gestion_producto.html'),
    path('empleado/listado-productos/', views.ProductoList, name='listado_productos.html'),
    path('empleado/gestion-proveedores/', views.ProveedorCreate, name='gestion_proveedores.html'),
    path('empleado/listado-proveedores/', views.ProveedorList, name='listado_proveedores.html'),
    path('empleado/gestion-contrato/', views.GestionContrato, name='gestion-contrato.html'),
    path('empleado/proceso-contrato/cliente/<int:id>/', views.ProcesoContrato, name='proceso-contrato.html'),
    path('empleado/listado-contrato/', views.ListContratos, name='listado-contrato.html'),
    path('empleado/detalle-contrato/<int:id>/', views.DetalleContrato, name='detalle-contrato.html'),
    path('empleado/gestion-pedidos/', views.GestionPedido, name='gestion-pedidos.html'),
    path('empleado/pedido/realizar/<int:id>/', views.ProcesoPedido, name ='realizar.html'),
    path('empleado/listado-pedidos/', views.ListadoPedido, name='listado-pedidos.html')
]