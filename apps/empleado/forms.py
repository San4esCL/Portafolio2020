from django.forms import *
from .models import Clientes


class ClienteForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    class Meta:
        model = Clientes
        fields = [
            'rut_empresa',
            'nombre_empresa',
            'razon_social',
            'direccion_empresa',
            'telefono_empresa',
            'contacto_empresa',
            'correo_empresa',
            'created_at'
        ]
