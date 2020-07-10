from django.db import models

# Create your models here.
class Clientes(models.Model):
    id_cliente = models.BigAutoField(primary_key=True)
    rut_empresa = models.CharField(max_length=15)
    nombre_empresa = models.CharField(max_length=100)
    razon_social = models.CharField(max_length=100)
    direccion_empresa = models.CharField(max_length=150)
    telefono_empresa = models.CharField(max_length=15)
    contacto_empresa = models.CharField(max_length=100, blank=True, null=True)
    correo_empresa = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'clientes'

class FamiliaProducto(models.Model):
    id_familia = models.BigAutoField(primary_key=True)
    tipo_familia = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'familia_producto'

class EstadoProducto(models.Model):
    id_estado_producto = models.BigAutoField(primary_key=True)
    estado_producto = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'estado_producto'

class Productos(models.Model):
    id_producto = models.BigAutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=255)
    precio_bruto = models.IntegerField()
    precio_venta =models.IntegerField()
    stock = models.IntegerField()
    stock_critico = models.IntegerField()
    id_familia = models.IntegerField()
    id_estado_producto = models.IntegerField()
    created_at = models.DateTimeField()
    id_proveedor = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'productos'

class ViewProductosDisponibles(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=255)
    precio_bruto = models.CharField(max_length=255)
    precio_venta =models.CharField(max_length=255)
    stock = models.IntegerField()
    stock_critico = models.IntegerField()
    familia = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'view_productos_disponibles'

class ViewProductosNoDisponibles(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=255)
    precio_bruto = models.CharField(max_length=255)
    precio_venta =models.CharField(max_length=255)
    stock = models.IntegerField()
    stock_critico = models.IntegerField()
    familia = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'view_productos_nodisponibles'



class Proveedor(models.Model):
    id_proveedor = models.BigAutoField(primary_key=True)
    nombre_prov = models.CharField(max_length=100)
    direccion_prov = models.CharField(max_length=100)
    fono_prov = models.CharField(max_length=15)
    email_prov = models.CharField(max_length=50, blank=True, null=True)
    id_rumbo_prov = models.IntegerField()
    id_usuario = models.IntegerField(null=True)
    created_at = models.DateTimeField()
    id_estadoprov = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'proveedores'

class EstadoProveedor(models.Model):
    id_estadoprov = models.BigAutoField(primary_key=True)
    estado_prov = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'estado_proveedor'

class RumboProveedor(models.Model):
    id_rumbo_prov = models.BigAutoField(primary_key=True)
    rumbo_prov = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'rumbo_proveedor'

class ViewProveedores(models.Model):
    id_proveedor = models.BigAutoField(primary_key=True)
    nombre_prov = models.CharField(max_length=100)
    rumbo_prov = models.CharField(max_length=100)
    fono_prov = models.CharField(max_length=15)
    direccion_prov = models.CharField(max_length=15)
    email_prov = models.CharField(max_length=50, blank=True, null=True)
    estado_prov = models.CharField(max_length=30)
    cant_pedidos = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'view_proveedores'

class Huespedes(models.Model):
    id_huesped = models.BigAutoField(primary_key=True)
    rut_huesped = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    fecha_ingreso = models.DateTimeField()
    nombres = models.CharField(max_length=100)
    id_cliente = models.BigIntegerField()
    id_estado_huesped = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'huespedes'

class ViewClientes(models.Model):
    id_cliente = models.BigAutoField(primary_key=True)
    empresa = models.CharField(max_length=255)
    rut = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    ingreso = models.DateField()
    cant_huespedes = models.IntegerField()
    huespedes_vigentes = models.IntegerField()
    contratos_vigentes = models.IntegerField()
    contratos_novigentes = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'view_cliente_cantidades'

class TipoContrato(models.Model):
    id_tipo_contrato = models.AutoField(primary_key=True)
    tipo_contrato = models.CharField(max_length=255)
    descripcion_contrato = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'tipo_contrato'

class Contrato(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    id_cliente = models.IntegerField()
    fecha_inicio_contrato = models.DateTimeField()
    id_estado_contrato = models.IntegerField()
    id_tipo_contrato = models.IntegerField()
    fecha_vencimiento = models.DateTimeField(blank=True,null=True)
    cantidad_huespedes = models.IntegerField()
    created_at = models.DateTimeField()
    duracion_contrato = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'contrato'

class contrato_huespedes(models.Model):
    id = models.AutoField(primary_key=True)
    id_contrato = models.IntegerField()
    id_huesped = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'contrato_huespedes'

class HabitacionesDisponibles(models.Model):
    id_habitacion = models.AutoField(primary_key=True)
    tipo_habitacion = models.CharField(max_length=255)
    precio_hab = models.CharField(max_length=255)
    banno_privado = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'view_habitaciones_disponibles'

class contrato_habitaciones(models.Model):
    id = models.AutoField(primary_key=True)
    id_contrato = models.IntegerField()
    id_habitacion = models.IntegerField()
    precio_Hab = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'contrato_habitacion'

class ViewContratos(models.Model):
    id_contrato = models.IntegerField(primary_key=True)
    empresa = models.CharField(max_length=255)
    tipo_contrato = models.CharField(max_length=255)
    fecha_inicio_contrato = models.DateField()
    fecha_vencimiento = models.CharField(max_length=255)
    cant_huesp = models.IntegerField()
    estado_contrato = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'view_contratos'

class ViewPedidosProductos(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre_prov = models.CharField(max_length=255)
    nombre_producto = models.CharField(max_length=255)
    tipo_familia = models.CharField(max_length=255)
    precio_bruto = models.IntegerField()
    stock = models.IntegerField()
    id_proveedor = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'view_productos_prov'

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    total_pedido = models.BigIntegerField()
    fecha_pedido = models.DateTimeField()
    id_proveedor = models.IntegerField()
    id_estadopedido = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'pedido'

class PedidoProducto(models.Model):
    id_pedido = models.IntegerField(primary_key=True)
    id_proveedor = models.IntegerField()
    id_producto = models.IntegerField()
    costo_bruto = models.IntegerField()
    cantidad = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'pedido_producto'

class ViewPedidos(models.Model):
    id_pedido = models.IntegerField(primary_key=True)
    fechaped = models.CharField(max_length=255)
    prov = models.CharField(max_length=255)
    cant_productos = models.IntegerField()
    total_pedido = models.CharField(max_length=255)
    estado_pedido = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'view_pedidos'

class ViewHuespedes(models.Model):
    rut_huesped = models.CharField(primary_key=True, max_length=255)
    nombres = models.CharField(max_length=255)
    fechanac = models.DateField()
    empresa = models.CharField(max_length=255)
    fonoempresa = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'view_huespedes'