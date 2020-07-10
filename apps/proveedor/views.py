from django.shortcuts import render
from .models import *
# Create your views here.


def home_proveedor(request):
    return render(request, 'base_proveedor.html')