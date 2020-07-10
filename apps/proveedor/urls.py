from django.urls import path
from . import views

app_name = 'proveedor'
# Las URL del empleado aca

urlpatterns = [
    path('proveedor/', views.home_proveedor, name='base_proveedor.html')
    ]