# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Clientes(models.Model):
    id_cliente = models.BigAutoField(primary_key=True)
    rut_empresa = models.CharField(max_length=15)
    nombre_empresa = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=100)
    direccion_empresa = models.CharField(max_length=150)
    telefono_empresa = models.CharField(max_length=15)
    contacto_empresa = models.CharField(max_length=100, blank=True, null=True)
    correo_empresa = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'clientes'


class Contrato(models.Model):
    id_contrato = models.BigAutoField(primary_key=True)
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente')
    fecha_inicio_contrato = models.DateTimeField()
    id_estado_contrato = models.ForeignKey('EstadoContrato', models.DO_NOTHING, db_column='id_estado_contrato')
    id_tipo_contrato = models.ForeignKey('TipoContrato', models.DO_NOTHING, db_column='id_tipo_contrato')
    fecha_vencimiento = models.DateTimeField()
    cantidad_huespedes = models.BigIntegerField()
    fecha_creacion = models.DateTimeField(db_column='fecha_creación')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contrato'


class ContratoHabitacion(models.Model):
    id_cuenta_contrato = models.OneToOneField('CuentaContrato', models.DO_NOTHING, db_column='id_cuenta_contrato', primary_key=True)
    id_habitacion = models.ForeignKey('Habitaciones', models.DO_NOTHING, db_column='id_habitacion')
    precio_hab = models.BigIntegerField()
    fecha_hab = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'contrato_habitacion'


class ContratoHuespedes(models.Model):
    id_contrato = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='id_contrato')
    id_huesped = models.ForeignKey('Huespedes', models.DO_NOTHING, db_column='id_huesped')

    class Meta:
        managed = False
        db_table = 'contrato_huespedes'


class ContratoPlato(models.Model):
    id_cuenta_contrato = models.ForeignKey('CuentaContrato', models.DO_NOTHING, db_column='id_cuenta_contrato')
    id_plato = models.ForeignKey('Plato', models.DO_NOTHING, db_column='id_plato')
    precio_plato = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'contrato_plato'


class ContratoProducto(models.Model):
    id_cuenta_contrato = models.ForeignKey('CuentaContrato', models.DO_NOTHING, db_column='id_cuenta_contrato')
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto')
    precio_prod = models.BigIntegerField()
    cantidad_prod = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'contrato_producto'


class ContratosPredefinidos(models.Model):
    id_contrato_predefinido = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'contratos_predefinidos'


class CuentaContrato(models.Model):
    id_cuenta_contrato = models.BigAutoField(primary_key=True)
    id_contrato = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='id_contrato')

    class Meta:
        managed = False
        db_table = 'cuenta_contrato'


class DetalleFactura(models.Model):
    id_detalle_factura = models.BigAutoField(primary_key=True)
    id_factura = models.ForeignKey('Factura', models.DO_NOTHING, db_column='id_factura')

    class Meta:
        managed = False
        db_table = 'detalle_factura'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleados(models.Model):
    id_empleado = models.BigAutoField(primary_key=True)
    rut_emp = models.CharField(max_length=10)
    nombres_emp = models.CharField(max_length=100)
    apellidos_emp = models.CharField(max_length=100)
    fono_emp = models.CharField(max_length=15)
    email_emp = models.CharField(max_length=50, blank=True, null=True)
    fechanac_emp = models.DateTimeField()
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario')
    id_estadoempleado = models.ForeignKey('EstadoEmpleado', models.DO_NOTHING, db_column='id_estadoempleado')
    id_tipoempleado = models.ForeignKey('TipoEmpleado', models.DO_NOTHING, db_column='id_tipoempleado')

    class Meta:
        managed = False
        db_table = 'empleados'


class EstadoContrato(models.Model):
    id_estado_contrato = models.BigAutoField(primary_key=True)
    estado_contrato = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estado_contrato'


class EstadoEmpleado(models.Model):
    id_estadoempleado = models.BigAutoField(primary_key=True)
    estado_empleado = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'estado_empleado'


class EstadoHabitacion(models.Model):
    id_estado_habitacion = models.BigAutoField(primary_key=True)
    estado_habitacion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'estado_habitacion'


class EstadoHostal(models.Model):
    id_estado_hostal = models.BigAutoField(primary_key=True)
    estado_hostal = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'estado_hostal'


class EstadoHuespedes(models.Model):
    id_estado_huesped = models.BigAutoField(primary_key=True)
    estado_huesped = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'estado_huespedes'


class EstadoPedido(models.Model):
    id_estadopedido = models.BigAutoField(primary_key=True)
    estado_pedido = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'estado_pedido'


class EstadoProducto(models.Model):
    id_estado_producto = models.BigAutoField(primary_key=True)
    estado_producto = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'estado_producto'


class EstadoProveedor(models.Model):
    id_estadoprov = models.BigAutoField(primary_key=True)
    estado_prov = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'estado_proveedor'


class EstadoUsuario(models.Model):
    id_estado_usuario = models.BigAutoField(primary_key=True)
    estado_usuario = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'estado_usuario'


class Factura(models.Model):
    id_factura = models.BigAutoField(primary_key=True)
    id_contrato = models.BigIntegerField()
    valor_total = models.BigIntegerField()
    fecha_factura = models.DateTimeField()
    hostal = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    telefono = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'factura'


class FamiliaProducto(models.Model):
    id_familia = models.BigAutoField(primary_key=True)
    tipo_familia = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'familia_producto'


class Habitaciones(models.Model):
    id_habitacion = models.BigAutoField(primary_key=True)
    id_hostal = models.BigIntegerField()
    tamanno_hab = models.CharField(max_length=100, blank=True, null=True)
    camas_hab = models.SmallIntegerField()
    banno_privado = models.CharField(max_length=1)
    precio_hab = models.BigIntegerField()
    id_estado_habitacion = models.ForeignKey(EstadoHabitacion, models.DO_NOTHING, db_column='id_estado_habitacion')
    id_tipohabitacion = models.ForeignKey('TipoHabitacion', models.DO_NOTHING, db_column='id_tipohabitacion')

    class Meta:
        managed = False
        db_table = 'habitaciones'


class Hostal(models.Model):
    id_hostal = models.BigAutoField(primary_key=True)
    nombre_hostal = models.CharField(max_length=100)
    direccion_hostal = models.CharField(max_length=100)
    id_estado_hostal = models.ForeignKey(EstadoHostal, models.DO_NOTHING, db_column='id_estado_hostal')

    class Meta:
        managed = False
        db_table = 'hostal'


class Huespedes(models.Model):
    id_huesped = models.BigAutoField(primary_key=True)
    rut_huesped = models.CharField(max_length=10)
    fecha_nacimiento = models.DateTimeField()
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente')
    id_estado_huesped = models.ForeignKey(EstadoHuespedes, models.DO_NOTHING, db_column='id_estado_huesped')

    class Meta:
        managed = False
        db_table = 'huespedes'


class Pedido(models.Model):
    id_pedido = models.BigAutoField(primary_key=True)
    total_pedido = models.BigIntegerField(blank=True, null=True)
    fecha_pedido = models.DateTimeField()
    id_empleado = models.ForeignKey(Empleados, models.DO_NOTHING, db_column='id_empleado')
    id_proveedor = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='id_proveedor')
    id_estadopedido = models.ForeignKey(EstadoPedido, models.DO_NOTHING, db_column='id_estadopedido')

    class Meta:
        managed = False
        db_table = 'pedido'


class PedidoProducto(models.Model):
    id_pedido = models.ForeignKey(Pedido, models.DO_NOTHING, db_column='id_pedido')
    id_proveedor = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='id_proveedor')
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto')
    costo_bruto = models.BigIntegerField()
    cantidad = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'pedido_producto'


class Plato(models.Model):
    id_plato = models.BigAutoField(primary_key=True)
    nombre_plato = models.CharField(max_length=100)
    precio_plato = models.BigIntegerField()
    id_tipo_plato = models.ForeignKey('TipoPlato', models.DO_NOTHING, db_column='id_tipo_plato')

    class Meta:
        managed = False
        db_table = 'plato'


class Productos(models.Model):
    id_producto = models.BigAutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    precio_bruto = models.BigIntegerField()
    precio_venta = models.BigIntegerField()
    stock = models.BigIntegerField()
    stock_critico = models.BigIntegerField()
    id_familia = models.ForeignKey(FamiliaProducto, models.DO_NOTHING, db_column='id_familia')
    id_estado_producto = models.ForeignKey(EstadoProducto, models.DO_NOTHING, db_column='id_estado_producto')

    class Meta:
        managed = False
        db_table = 'productos'


class Proveedores(models.Model):
    id_proveedor = models.BigAutoField(primary_key=True)
    nombre_prov = models.CharField(max_length=100)
    direccion_prov = models.CharField(max_length=100)
    fono_prov = models.CharField(max_length=15)
    email_prov = models.CharField(max_length=50, blank=True, null=True)
    id_rumbo_prov = models.ForeignKey('RumboProveedor', models.DO_NOTHING, db_column='id_rumbo_prov')
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    fecha_ingreso = models.DateTimeField()
    id_estadoprov = models.ForeignKey(EstadoProveedor, models.DO_NOTHING, db_column='id_estadoprov')

    class Meta:
        managed = False
        db_table = 'proveedores'


class RumboProveedor(models.Model):
    id_rumbo_prov = models.BigAutoField(primary_key=True)
    rumbo_prov = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'rumbo_proveedor'


class TipoContrato(models.Model):
    id_tipo_contrato = models.BigAutoField(primary_key=True)
    tipo_contrato = models.CharField(max_length=50)
    descripcion_contrato = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tipo_contrato'


class TipoEmpleado(models.Model):
    id_tipoempleado = models.BigAutoField(primary_key=True)
    tipo_empleado = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_empleado'


class TipoHabitacion(models.Model):
    id_tipohabitacion = models.BigAutoField(primary_key=True)
    tipo_habitacion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_habitacion'


class TipoPlato(models.Model):
    id_tipo_plato = models.BigAutoField(primary_key=True)
    tipo_plato = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tipo_plato'


class TipoUsuario(models.Model):
    id_tipo_usuario = models.BigAutoField(primary_key=True)
    tipo_usuario = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_usuario'


class Usuarios(models.Model):
    id_usuario = models.BigAutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=30)
    passwd_usuario = models.CharField(max_length=30)
    id_tipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='id_tipo_usuario')
    id_estado_usuario = models.ForeignKey(EstadoUsuario, models.DO_NOTHING, db_column='id_estado_usuario')

    class Meta:
        managed = False
        db_table = 'usuarios'
