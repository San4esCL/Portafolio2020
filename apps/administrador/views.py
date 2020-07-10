from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, UpdateView

from .forms import CustomUserForm
from django.contrib.auth.decorators import login_required, permission_required
from .models import ViewHabitaciones, Habitacion, TipoHabitacion, EstadoHabitacion, ViewEmpleados, Empleados, \
    TipoEmpleado, EstadoEmpleado


# Create your views here.

# Usuario
@login_required
def homeadmin(request):
    return render(request, "baseadmin.html")


@login_required
def adminusuario(request):
    data = {
        'form': CustomUserForm()

    }

    if request.method == 'POST':
        formulario = CustomUserForm(request)

    return render(request, 'usuario/Admin_Usuario.html', data)


@login_required
def listausuario(request):
    return render(request, 'usuario/Listado_Usuario.html')


# Habitacion
@login_required
def adminhabit(request):
    tiposhab = TipoHabitacion.objects.all()
    estadohab = EstadoHabitacion.objects.all()
    variables = {
        'tiposhab': tiposhab,
        'estadohab': estadohab
    }
    if request.method == 'POST':
        hab_tam = request.POST["txtTam"]
        hab_prec = request.POST["txtPrecio"]
        hab_banno = request.POST["cbobano"]
        hab_estado = request.POST["cboestado"]
        hab_tipo = request.POST["cbotipo"]
        habitacion = Habitacion(tamanno_hab=hab_tam, banno_privado=hab_banno, precio_hab=hab_prec,
                                id_estado_habitacion=hab_estado, id_tipohabitacion=hab_tipo)
        habitacion.save()
    return render(request, 'habitacion/addhab.html', variables)




class ViewListHabitacion(ListView):
    model = ViewHabitaciones
    template_name = 'habitacion/Listado_Habitacion.html'

    def post(self, request, *args, **kwargs):
        data = {}
        hab = Habitacion.objects.get(id_habitacion=request.POST['id'])
        hab.id_estado_habitacion = 3
        hab.save()
        data['Estado'] = hab.id_estado_habitacion
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['habitaciones'] = ViewHabitaciones.objects.all()
        return context

@login_required
def updatehabit(request, id):
    tiposhab = TipoHabitacion.objects.all()
    estadohab = EstadoHabitacion.objects.all()
    habi = Habitacion.objects.get(id_habitacion=id)
    variables = {
        'tiposhab': tiposhab,
        'estadohab': estadohab,
        'habi': habi
    }
    if request.method == 'POST':
        habi.tamanno_hab = request.POST["txtTam"]
        habi.precio_hab = request.POST["txtPrecio"]
        habi.banno_privado = request.POST["cbobano"]
        habi.id_estado_habitacion = request.POST["cboestado"]
        habi.id_tipohabitacion = request.POST["cbotipo"]
        habi.save()
    return render(request, 'habitacion/updatehab.html', variables)



# Empleado
@login_required
def adminempleado(request):
    tiposemp = TipoEmpleado.objects.all()
    estadoemp = EstadoEmpleado.objects.all()
    variables = {
        'tiposemp': tiposemp,
        'estadoemp': estadoemp
    }
    if request.method == 'POST':
        emp = Empleados()
        emp.rut_emp = request.POST['rut_emp']
        emp.id_tipoempleado = request.POST["cbotipo"]
        emp.id_estadoempleado = request.POST["cboestado"]
        emp.nombres_emp = request.POST["primernombre"] + " " + request.POST["segundonombre"]
        emp.apellidos_emp = request.POST["primerapellido"] + " " + request.POST["segundoapellido"]
        emp.fono_emp = request.POST['fono_emp']
        emp.email_emp = request.POST['email_emp']
        emp.fechanac_emp = request.POST['fechanac']
        emp.save()
    return render(request, 'empleados/addemp.html', variables)

class ViewListaEmpleado(ListView):
    model = ViewEmpleados
    template_name = 'empleados/Listado_Empleado.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['empleados'] = ViewEmpleados.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        emp = Empleados.objects.get(rut_emp=request.POST['rut'])
        emp.id_estadoempleado = 3
        emp.save()
        data['Estado emp'] = emp.id_estadoempleado
        return JsonResponse(data)

@login_required
def updateempleado(request, id):
    tiposemp = TipoEmpleado.objects.all()
    estadoemp = EstadoEmpleado.objects.all()
    emp = Empleados.objects.get(id_empleado=id)
    variables = {
        'tiposemp': tiposemp,
        'estadoemp': estadoemp,
        'emp': emp
    }
    if request.method == 'POST':
        emp.rut_emp = request.POST['rut_emp']
        emp.id_tipoempleado = request.POST["cbotipo"]
        emp.id_estadoempleado = request.POST["cboestado"]
        emp.nombres_emp = request.POST["nombres_emp"]
        emp.apellidos_emp = request.POST["apellidos_emp"]
        emp.fono_emp = request.POST['fono_emp']
        emp.email_emp = request.POST['email_emp']
        emp.fechanac_emp = request.POST['fechanac']
        emp.save(force_update=True)
    return render(request, 'empleados/updemp.html', variables)


@login_required
def pedidos(request):
    return render(request, 'informes/InformePedido.html')


def productos(request):
    return render(request, 'informes/InformeProductos.html')
