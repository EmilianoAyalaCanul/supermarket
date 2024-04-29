from django.conf import settings
from django.db import models

class Cliente(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    rfc = models.CharField(max_length=15,blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    codigo_postal = models.CharField(max_length=6, blank=True, null=True)
    ciudad = models.CharField(max_length=80, blank=True, null=True)
    estado = models.CharField(max_length=80, blank=True, null=True)
    telefono = models.CharField(max_length=50)
    email = models.EmailField(max_length=80, blank=True, null=True)
    monto_credito = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)


class Personal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    rfc = models.CharField(max_length=15,blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    codigo_postal = models.CharField(max_length=6, blank=True, null=True)
    ciudad = models.CharField(max_length=80, blank=True, null=True)
    estado = models.CharField(max_length=80, blank=True, null=True)
    telefono = models.CharField(max_length=50)
    email = models.EmailField(max_length=80, blank=True, null=True)
    puesto = models.CharField(max_length=80, blank=True, null=True)
    dapartamento = models.CharField(max_length=80, blank=True, null=True)   
    
    def __str__(self):
        return "{} {}".format(self.user.first_name, self.user.last_name)
    

class Supermercado(models.Model):
    nombre = models.CharField(max_length=80, blank=True, null=True)
    rfc = models.CharField(max_length=15,blank=True, null=True)
    telefono = models.CharField(max_length=50)
    direccion = models.TextField(blank=True, null=True)
    ciudad = models.CharField(max_length=80, blank=True, null=True)
    estado = models.CharField(max_length=80, blank=True, null=True)
    email = models.EmailField(max_length=80, blank=True, null=True)
    web = models.CharField(max_length=80, blank=True, null=True)
    iva = models.FloatField(blank=True, null=True)
    ganancia = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = models.CharField(max_length=80, blank=True, null=True)
    rfc = models.CharField(max_length=15,blank=True, null=True)
    codigo_postal = models.CharField(max_length=6, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    telefono = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=80, blank=True, null=True)
    estado = models.CharField(max_length=80, blank=True, null=True)
    email = models.EmailField(max_length=80, blank=True, null=True)
    contacto = models.TextField(max_length=80, blank=True, null=True)
    web = models.CharField(max_length=80, blank=True, null=True)
    

    def __str__(self):
        return self.nombre

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    proveedor = models.ForeignKey(Proveedor, null=True, blank=True, on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaProducto, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    marca = models.CharField(max_length=80, blank=True, null=True)
    costo = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    precio_publico = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    existencias = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)    
    is_excento_iva = models.BooleanField(default=False)    

    def __str__(self):
        return self.nombre


class Descuento(models.Model):
    producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
    porcentaje_descuento = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    activo = models.BooleanField(default=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)    
    fecha_fin= models.DateTimeField(blank=True, null=True)    

    def __str__(self):
        return self.producto.nombre


class Merma(models.Model):
    producto = models.ForeignKey(Producto, null=True, blank=True, on_delete=models.CASCADE)
    cantidad = models.IntegerField(blank=True, null=True, default=0)
    costo = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    monto = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)    

    def __str__(self):
        return self.producto.nombre


class Moneda(models.Model):
    nombre = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.nombre

class FormaPago(models.Model):
    nombre = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.nombre

class MetodoPago(models.Model):
    nombre = models.CharField(max_length=80, blank=True, null=True)
    is_credito = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre


class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)    
    subtotal = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    impuesto = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    forma_pago = models.ForeignKey(FormaPago, on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.fecha, self.proveedor.nombre)


class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    precio_unitario = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    importe = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    descuento = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    impuesto = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)    



class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)    
    fecha = models.DateTimeField(auto_now_add=True, blank=True)
    total_piezas = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    subtotal = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    impuesto = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
    forma_pago = models.ForeignKey(FormaPago, on_delete=models.CASCADE)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} {}".format(self.fecha, self.cliente.user.first_name, self.cliente.user.last_name)


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    precio_unitario = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    importe = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    descuento = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    impuesto = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)


class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)    
    is_cancelado = models.BooleanField(default=False)
    
    def __str__(self):
        return "{} - {} {}".format(self.fecha, self.cliente.user.first_name, self.cliente.user.last_name)

class Deuda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    fecha_limite = models.DateField()


class PagoDeuda(models.Model):
    deuda = models.ForeignKey(Deuda, on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField(auto_now_add=True, blank=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    saldo = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
