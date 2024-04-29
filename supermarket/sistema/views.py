from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import FormView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db import transaction
import datetime

def index(request):    
    return render(request, 'cliente/index.html')
    

@transaction.atomic
def registroCliente(request):
    if request.method == "POST":
        try:
            user_sistema = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
            user_sistema.last_name = request.POST['last_name']
            user_sistema.first_name = request.POST['first_name']
            user_sistema.save()
            
            cliente = Cliente(
                user = user_sistema,
                rfc = request.POST['rfc'],
                direccion = request.POST['direccion'],
                codigo_postal = request.POST['codigo_postal'],
                ciudad = request.POST['ciudad'],
                estado = request.POST['estado'],
                telefono = request.POST['telefono'],
                email = request.POST['email'],
                monto_credito = 0
            )
            cliente.save()
            
            messages.success(request, 'Usuario registrado correctamente. Favor de loguearte.')
            return redirect('login')
        
        except Exception as error:            
            transaction.set_rollback(True)            
            dato = "Ocurrio un problema al registrar: {0}".format(str(error.args))            
            messages.error(request, dato)
            
    return render(request, 'administracion/registro.html')


@login_required(login_url="login")
def agregarCarrito(request):    
    productos = Producto.objects.filter(activo = True)
    contexto = {'productos': productos}

    if request.POST:
        if not 'compra' in request.session:                 
            request.session['compra'] = {}    

        for producto in productos:        
            identificador_producto = "producto_{}".format(producto.id)
            if identificador_producto in request.POST:
                cantidad_producto = request.POST[identificador_producto]
                if identificador_producto in request.session['compra']:
                    request.session['compra'][identificador_producto]['cantidad'] = int(request.session['compra'][identificador_producto]['cantidad']) + int(cantidad_producto) 
                else:
                    if int(cantidad_producto) > 0:
                        request.session['compra'][identificador_producto] = {
                            'id_producto': producto.id,
                            'cantidad': cantidad_producto
                        }

        messages.success(request, "Agregado al carrito de compra")
        return render(request, 'cliente/comprar_productos.html', contexto)
    else:        
        return render(request, 'cliente/comprar_productos.html', contexto)


@login_required(login_url="login")
@transaction.atomic
def carrito(request):    
    #Captura de la venta
    if request.POST:
        try:
            cliente = Cliente.objects.get(user = request.user)
            moneda_seleccionada = Moneda.objects.get(id = request.POST['moneda'])
            forma_pago_seleccionada = FormaPago.objects.get(id = request.POST['forma_pago'])
            metodo_pago_seleccionada = MetodoPago.objects.get(id = request.POST['metodo_pago'])
            venta = Venta(
                cliente = cliente,
                total_piezas = request.session['detalle_global']['cantidad_global'], 
                subtotal = request.session['detalle_global']['subtotal_global'], 
                impuesto = request.session['detalle_global']['impuesto_global'], 
                total = request.session['detalle_global']['total_global'], 
                moneda = moneda_seleccionada,
                forma_pago =forma_pago_seleccionada,
                metodo_pago = metodo_pago_seleccionada
            )
            venta.save()

            if metodo_pago_seleccionada.is_credito:
                #Registro deuda
                fecha_limite = datetime.datetime.now() + datetime.timedelta(days=30)
                deuda = Deuda(
                    cliente = cliente,
                    venta = venta,
                    total = request.session['detalle_global']['total_global'], 
                    fecha_limite = fecha_limite
                )
                deuda.save()

            
            
                #Registro Factura
            fecha_limite = datetime.datetime.now() + datetime.timedelta(days=30)
            factura = Factura(
                cliente = cliente,
                venta = venta                
            )
            factura.save()

            #Registro detalle venta
            for value in request.session['compra_formato']: 
                producto_registrado = Producto.objects.get(id = value['id'])                
                registro_detalleventa = DetalleVenta(
                    venta = venta,
                    producto = producto_registrado,    
                    cantidad = value['cantidad'],
                    precio_unitario = producto_registrado.precio_publico,
                    importe = value['subtotal'],
                    descuento = 0,
                    impuesto = value['impuesto'],
                    total = value['total']
                )
                registro_detalleventa.save()
            request.session['compra_formato'] = {}
            request.session['detalle_global'] = {}
            request.session['compra'] = {}
            messages.success(request, "Compra realizada satisfactoriamente!")
            return redirect('sistema:mis_compras')    
        except Exception as error:            
            transaction.set_rollback(True)    
            print(error)        
            dato = "Ocurrio un problema al registrar la venta: {0}".format(str(error.args))            
            messages.error(request, dato)
            return redirect('sistema:mis_compras')
    else:
        productos = Producto.objects.filter(activo = True)
        supermercado = Supermercado.objects.all().last()
        moneda = Moneda.objects.all()
        forma_pago = FormaPago.objects.all()
        metodo_pago = MetodoPago.objects.all()
        contexto = {}    
        compra = []
        cantidad_global = 0
        subtotal_global = 0    
        impuesto_global = 0
        total_global = 0

        if 'compra' in request.session:
            if request.session['compra']:
                for producto in productos:        
                    identificador_producto = "producto_{}".format(producto.id)    
                    if identificador_producto in request.session['compra']:
                        cantidad = int(request.session['compra'][identificador_producto]['cantidad'])                    
                        iva = float(supermercado.iva/100)
                        subtotal = float( cantidad * producto.precio_publico)                    
                        if producto.is_excento_iva:
                            impuesto = 0
                        else:
                            impuesto = float(subtotal) * float(iva)                    
                        total = float(subtotal) + float(impuesto)
                        cantidad_global += cantidad
                        subtotal_global += subtotal
                        impuesto_global += impuesto
                        total_global += total
                        compra.append( {
                            "id": producto.id,
                            "nombre": producto.nombre,
                            "cantidad": cantidad,
                            "subtotal": subtotal,
                            "impuesto": impuesto,
                            "total": total                        
                            }
                        )
        contexto['compra'] = compra
        request.session['compra_formato'] = compra
        request.session['detalle_global'] = {
            'cantidad_global':cantidad_global,
            'subtotal_global':subtotal_global,
            'impuesto_global':impuesto_global,
            'total_global':total_global
            }
        contexto['cantidad_global']=cantidad_global
        contexto['subtotal_global']=subtotal_global
        contexto['impuesto_global']=impuesto_global
        contexto['total_global']=total_global
        contexto['moneda']=moneda
        contexto['forma_pago']=forma_pago
        contexto['metodo_pago']=metodo_pago
        return render(request, 'cliente/carrito.html', contexto )


@login_required(login_url="login")
def cancelarCarrito(request):    
    request.session['compra'] = {}    
    request.session['compra_formato'] = {}
    request.session['detalle_global'] = {}

    messages.warning(request, "Compra cancelada!")
    return redirect('sistema:agregar_carrito')


@login_required(login_url="login")
def verDeudas(request):
    user = request.user
    lista_deudas = Deuda.objects.filter(cliente__user = user)
    contexto = {"deudas": lista_deudas}    
    return render(request, 'cliente/lista_deudas.html', contexto )


@login_required(login_url="login")
def verFacturas(request):
    user = request.user
    lista_facturas = Factura.objects.filter(cliente__user = user)
    contexto = {"facturas": lista_facturas}    
    return render(request, 'cliente/lista_facturas.html', contexto )


@login_required(login_url="login")
def verMisCompras(request):
    user = request.user    
    lista_facturas = Venta.objects.filter(cliente__user = user)
    contexto = {"compras": lista_facturas}    
    return render(request, 'cliente/lista_compras.html', contexto )


