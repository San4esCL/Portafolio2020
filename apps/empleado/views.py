from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

from django.views.generic import ListView

from ..administrador.models import Habitacion
from .models import *


# Mis Vistas


def home_empleado(request):
    return render(request, "base_empleado.html")


# Clientes

def ClienteList(request):
    data = {
        'clientes': Clientes.objects.all()
    }
    return render(request, 'Cliente/listado_cliente.html', data)


class ClienteListView(ListView):
    model = Clientes
    template_name = 'Cliente/listado_cliente.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


def ClienteCreate(request):
    data = {}
    data['hoy'] = datetime.now()
    if request.method == 'POST':
        try:
            cli = Clientes()
            cli.rut_empresa = request.POST["rut_empresa"]
            cli.nombre_empresa = request.POST["nombre_empresa"]
            cli.razon_social = request.POST["razon_social"]
            cli.direccion_empresa = request.POST["direccion_empresa"]
            cli.telefono_empresa = request.POST["telefono_empresa"]
            cli.contacto_empresa = request.POST["contacto_empresa"]
            cli.correo_empresa = request.POST["correo_empresa"]
            cli.created_at = datetime.now()
            cli.save()
            print('paso')
            data = {}
            return JsonResponse(data)
        except Exception as e:
            data['error'] = str(e)
            return JsonResponse(data)
    return render(request, 'Cliente/gestion_cliente.html', data)


def ProductoCreate(request):
    datos = {}
    famprod = FamiliaProducto.objects.all()
    estaprod = EstadoProducto.objects.all()
    prov = Proveedor.objects.all()
    data = {
        'famprod': famprod,
        'estaprod': estaprod,
        'hoy': datetime.now(),
        'prov': prov
    }
    if request.method == 'POST':
        try:
            prod = Productos()
            prod.nombre_producto = request.POST["nombre_producto"]
            prod.id_familia = request.POST["id_familia"]
            prod.precio_bruto = request.POST["precio_bruto"]
            prod.precio_venta = request.POST["precio_venta"]
            prod.stock = request.POST["stock"]
            prod.stock_critico = request.POST["stock_critico"]
            prod.id_estado_producto = request.POST["id_estado_producto"]
            prod.id_proveedor = request.POST['id_proveedor']
            prod.created_at = datetime.now()
            prod.save()
            print("paso")
            return JsonResponse(datos)
        except Exception as e:
            datos['error'] = str(e)
            return JsonResponse(datos)
    return render(request, 'Productos/gestion_productos.html', data)


def ProductoList(request):
    prod_disp = ViewProductosDisponibles.objects.all()
    prod_nodisp = ViewProductosNoDisponibles.objects.all()
    variables = {
        'prod_disp': prod_disp,
        'prod_nodisp': prod_nodisp
    }
    return render(request, 'Productos/listado_productos.html', variables)


def ProveedorList(request):
    viewprov = ViewProveedores.objects.all()
    variables = {
        'viewprov': viewprov
    }
    return render(request, 'Proveedor/listado_proveedores.html', variables)


def ProveedorCreate(request):
    datos = {}
    rubro = RumboProveedor.objects.all()
    estadoprov = EstadoProveedor.objects.all()
    variables = {
        'rubro': rubro,
        'estadoprov': estadoprov,
        'hoy': datetime.now()
    }

    if request.method == 'POST':
        try:
            prov = Proveedor()
            prov.nombre_prov = request.POST["nombre_prov"]
            prov.direccion_prov = request.POST["direccion_prov"]
            prov.fono_prov = request.POST["fono_prov"]
            prov.email_prov = request.POST["email_prov"]
            prov.id_rumbo_prov = request.POST["id_rumbo_prov"]
            prov.created_at = datetime.now()
            prov.id_estadoprov = request.POST["id_estadoprov"]
            prov.save()
            print("paso")
            return JsonResponse(datos)
        except Exception as e:
            datos['error'] = str(e)
            return JsonResponse(datos)
    return render(request, 'Proveedor/gestion_proveedores.html', variables)


def GestionContrato(request):
    cli = Clientes.objects.all()
    variables = {
        'cli': cli
    }
    return render(request, 'Contrato/gestion-contrato.html', variables)


def ProcesoContrato(request, id):
    huesp = Huespedes.objects.filter(id_cliente=id)
    clienteinfo = ViewClientes.objects.filter(id_cliente=id)
    tipocon = TipoContrato.objects.all()
    habidisp = HabitacionesDisponibles.objects.all()
    variables = {
        'huesp': huesp,
        'clienteinfo': clienteinfo,
        'tipocon': tipocon,
        'habidisp': habidisp,
        'hoy': datetime.now()
    }
    datos = {}
    if request.method == 'POST':
        try:
            print(request.POST)
            con = Contrato()
            con.id_cliente = id
            con.fecha_inicio_contrato = request.POST['fecha_inicio']
            con.id_estado_contrato = 3
            con.id_tipo_contrato = request.POST['id_tipo_contrato']
            con.fecha_vencimiento = None
            con.cantidad_huespedes = int(request.POST['cant_huesp'])
            con.created_at = datetime.now()
            con.duracion_contrato = int(request.POST['cant_dias'])
            con.save()
            print(con.id_contrato)

            huespedes = request.POST.getlist('id_huesped')
            print(huespedes)
            for x in huespedes:
                conhsp = contrato_huespedes()
                conhsp.id_contrato = con.id_contrato
                conhsp.id_huesped = x
                conhsp.save()
                print('ID Contrato', conhsp.id_contrato, 'ID Huesped: ', conhsp.id_huesped)

            habitaciones = request.POST.getlist('id_habitacion')
            print(habitaciones)
            for x in habitaciones:
                hab = Habitacion.objects.get(id_habitacion=x)
                conhab = contrato_habitaciones()
                conhab.id_contrato = con.id_contrato
                conhab.id_habitacion = x
                conhab.precio_Hab = hab.precio_hab
                conhab.save()
            return JsonResponse(datos)
        except Exception as e:

            datos['error'] = str(e)
            return JsonResponse(datos)

    return render(request, 'Contrato/proceso-contrato.html', variables)


def ListContratos(request):
    variables = {
        'contratos': ViewContratos.objects.all()
    }
    return render(request, 'Contrato/listado-contrato.html', variables)


def DetalleContrato(request, id):
    variables = {}
    return render(request, 'Contrato/detalle-contrato.html', variables)


def GestionPedido(request):
    variables = {
        'prov': ViewProveedores.objects.all()
    }
    return render(request, 'Pedido/proceso-pedidos.html', variables)


def ProcesoPedido(request, id):
    datos = {}
    prod = ViewPedidosProductos.objects.filter(id_proveedor=id)
    variables = {
        'prod': prod
    }
    if request.method == 'POST':
        try:
            print(request.POST)
            ped = Pedido()
            ped.id_proveedor = id
            ped.fecha_pedido = datetime.now()
            ped.id_estadopedido = 1
            ped.save()

            produ = request.POST.getlist('id_producto')
            cants = request.POST.getlist('cantidad')
            for x, y in zip(produ, cants):
                pdto = Productos.objects.get(id_producto=x)
                prodpedido = PedidoProducto()
                prodpedido.id_pedido = ped.id_pedido
                prodpedido.id_proveedor = id
                prodpedido.id_producto = x
                prodpedido.costo_bruto = pdto.precio_bruto
                prodpedido.cantidad = y
                prodpedido.save(force_insert=True)
                print('ID PEDIDO: ', ped.id_pedido, ' ID PROVEEDOR: ', id, ' ID PRODUCTO: ', x, ' COSTO BRUTO: ',
                      pdto.precio_bruto, ' CANTIDAD: ', y)
            return JsonResponse(datos)
        except Exception as e:
            datos['error'] = str(e)
            return JsonResponse(datos)


    return render(request, 'Pedido/realizar.html', variables)


def ListadoPedido(request):
    listped = ViewPedidos.objects.all()
    variables = {
        'listped': listped
    }
    return render(request, 'Pedido/listado-pedidos.html', variables)

def HuespedesList(request):
    huesp = ViewHuespedes.objects.all()
    variables = {
        'huesp':huesp
    }
    return render(request, 'Huespedes/huespedes.html', variables)