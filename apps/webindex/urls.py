from django.urls import path
from . import views

urlpatterns = [
    path('', views.web, name='inicio.html'),
    
    
]