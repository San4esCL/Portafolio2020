from django.urls import path
from . import views


urlpatterns = [
    path('administrador/', views.homeadmin, name='baseadmin.html'),

    path('adminusuario/',  views.adminusuario, name='adminusuario.html'),
    path('listadousuario/',  views.listausuario, name='listadousuario.html'),

    path('administrador/adminhabit/', views.adminhabit, name='addhab.html'),
    path('administrador/listahabitacion/', views.ViewListHabitacion.as_view(), name='Listado_Habitacion.html'),
    path('administrador/updhabitacion/<int:id>/', views.updatehabit, name='updatehab.html'),

    path('administrador/adminemp/',  views.adminempleado, name='addemp.html'),
    path('administrador/listaempleado/',  views.ViewListaEmpleado.as_view(), name='Listado_Empleado.html'),
    path('administrador/updempleado/<int:id>/',  views.updateempleado, name='updeemp.html'),


    path('administrador/informes/pedidos/',  views.pedidos, name='InformePedido.html'),
    path('productos/',  views.productos, name='InformeProductos.html'),
    

]