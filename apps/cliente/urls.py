from django.urls import path
from . import views

urlpatterns = [
    path('cliente/', views.homecli, name='base_cliente.html')
]