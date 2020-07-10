from django.db import models


# Create your models here.
class ViewHabitaciones(models.Model):
    id_habitacion = models.IntegerField(primary_key=True)
    tipo_habitacion = models.CharField(max_length=255)
    Precio = models.CharField(max_length=255)
    tamanno_hab = models.CharField(max_length=255)
    banno = models.CharField(max_length=255)
    estado_habitacion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'view_habitaciones'  # your view name


class Habitacion(models.Model):
    id_habitacion = models.AutoField(primary_key=True)
    tamanno_hab = models.CharField(max_length=100)
    banno_privado = models.CharField(max_length=1)
    precio_hab = models.BigIntegerField()
    id_estado_habitacion = models.BigIntegerField()
    id_tipohabitacion = models.BigIntegerField()

    class Meta:
        managed = True
        db_table = 'habitaciones'  # your view name


class TipoHabitacion(models.Model):
    id_tipohabitacion = models.BigAutoField(primary_key=True)
    tipo_habitacion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_habitacion'


class EstadoHabitacion(models.Model):
    id_estado_habitacion = models.BigAutoField(primary_key=True)
    estado_habitacion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'estado_habitacion'


class ViewEmpleados(models.Model):
    id_empleado = models.IntegerField(primary_key=True)
    rut_emp = models.CharField(max_length=255)
    tipo_empleado = models.CharField(max_length=255)
    nombres_emp = models.CharField(max_length=255)
    apellidos_emp = models.CharField(max_length=255)
    FECHANAC = models.DateField()
    fono_emp = models.CharField(max_length=255)
    email_emp = models.CharField(max_length=255)
    estado_empleado = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'view_empleados'  # your view name


class Empleados(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    rut_emp = models.CharField(max_length=255)
    nombres_emp = models.CharField(max_length=255)
    apellidos_emp = models.CharField(max_length=255)
    fono_emp = models.CharField(max_length=255)
    email_emp = models.CharField(max_length=255)
    fechanac_emp = models.DateField()
    id_estadoempleado = models.IntegerField()
    id_tipoempleado = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'empleados'


class TipoEmpleado(models.Model):
    id_tipoempleado = models.IntegerField(primary_key=True)
    tipo_empleado = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'tipo_empleado'


class EstadoEmpleado(models.Model):
    id_estadoempleado = models.IntegerField(primary_key=True)
    estado_empleado = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'estado_empleado'
        ordering = ['id_estadoempleado']
