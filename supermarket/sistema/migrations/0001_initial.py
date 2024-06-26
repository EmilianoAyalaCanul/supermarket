# Generated by Django 5.0.4 on 2024-04-28 21:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FormaPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=80, null=True)),
                ('is_credito', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=80, null=True)),
                ('rfc', models.CharField(blank=True, max_length=15, null=True)),
                ('codigo_postal', models.CharField(blank=True, max_length=6, null=True)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('telefono', models.CharField(max_length=50)),
                ('ciudad', models.CharField(blank=True, max_length=80, null=True)),
                ('estado', models.CharField(blank=True, max_length=80, null=True)),
                ('email', models.EmailField(blank=True, max_length=80, null=True)),
                ('contacto', models.TextField(blank=True, max_length=80, null=True)),
                ('web', models.CharField(blank=True, max_length=80, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supermercado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=80, null=True)),
                ('rfc', models.CharField(blank=True, max_length=15, null=True)),
                ('telefono', models.CharField(max_length=50)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=80, null=True)),
                ('estado', models.CharField(blank=True, max_length=80, null=True)),
                ('email', models.EmailField(blank=True, max_length=80, null=True)),
                ('web', models.CharField(blank=True, max_length=80, null=True)),
                ('iva', models.FloatField(blank=True, null=True)),
                ('ganancia', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfc', models.CharField(blank=True, max_length=15, null=True)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('codigo_postal', models.CharField(blank=True, max_length=6, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=80, null=True)),
                ('estado', models.CharField(blank=True, max_length=80, null=True)),
                ('telefono', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=80, null=True)),
                ('monto_credito', models.FloatField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deuda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('fecha_limite', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='PagoDeuda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('saldo', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('deuda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.deuda')),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfc', models.CharField(blank=True, max_length=15, null=True)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('codigo_postal', models.CharField(blank=True, max_length=6, null=True)),
                ('ciudad', models.CharField(blank=True, max_length=80, null=True)),
                ('estado', models.CharField(blank=True, max_length=80, null=True)),
                ('telefono', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=80, null=True)),
                ('puesto', models.CharField(blank=True, max_length=80, null=True)),
                ('dapartamento', models.CharField(blank=True, max_length=80, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('impuesto', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('forma_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.formapago')),
                ('metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.metodopago')),
                ('moneda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.moneda')),
                ('personal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.personal')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=80, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('marca', models.CharField(blank=True, max_length=80, null=True)),
                ('costo', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('precio_publico', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('existencias', models.IntegerField(default=0)),
                ('activo', models.BooleanField(default=True)),
                ('is_excento_iva', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.categoriaproducto')),
                ('proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Merma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(blank=True, default=0, null=True)),
                ('costo', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('monto', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.producto')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('precio_unitario', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('importe', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('descuento', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('impuesto', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porcentaje_descuento', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('activo', models.BooleanField(default=True)),
                ('fecha_inicio', models.DateTimeField(blank=True, null=True)),
                ('fecha_fin', models.DateTimeField(blank=True, null=True)),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('total_piezas', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('impuesto', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.cliente')),
                ('forma_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.formapago')),
                ('metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.metodopago')),
                ('moneda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.moneda')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('is_cancelado', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.cliente')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.venta')),
            ],
        ),
        migrations.AddField(
            model_name='deuda',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.venta'),
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('precio_unitario', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('importe', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('descuento', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('impuesto', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.venta')),
            ],
        ),
    ]
