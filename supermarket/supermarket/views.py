from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.static import serve
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from sistema.models import *
import json

def index(request):
    return render(request, 'index.html')


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)     
        
        if user is not None:
            messages.success(request, 'Sesión iniciada correctamente.')
            login(request, user)            
            return redirect('sistema:index')
        else:
            messages.error(request, 'Usuario o Password incorrecto.')
			
    context = {}
    return render(request, 'administracion/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('index')


def cargaDatosInicial(request):    
    #DATOS GENERALES DEL SUPERMERCADO
    supermarket = Supermercado.objects.all()
    if not supermarket:
        supermarket = Supermercado(
            nombre = "PrimeMed Supply",
            rfc = "PRM150315XYZ",
            telefono = "9818133747",
            direccion = "Av. Revolución 348, Colonia Condesa, Código Postal: 06140",
            ciudad = "Ciudad de México",
            estado = "Ciudad de México",
            email = "contacto@primemedsupply.mx",
            web = "www.primemedsupply.mx",
            iva = 16,
            ganancia = 30
        )
        supermarket.save()

    #DATOS GENERALES DE MODENA
    registro_moneda = Moneda.objects.all()
    if not registro_moneda:
        datos_moneda = {
            "moneda": [
                "Peso Mexicano",
                "Dólar Americano",
                "Euro",
                "Dólar Canadiense"
            ]
        }

        for moneda in datos_moneda["moneda"]:
            registro_moneda = Moneda(
                nombre = moneda
            )
            registro_moneda.save()

    #DATOS GENERALES DE TIPO PAGO
    registro_forma_pago = FormaPago.objects.all()
    if not registro_forma_pago:
        datos_forma_pago = {
            "forma_pago": [
                "Efectivo",
                "Transferencia",
                "Tarjeta Crédito",
                "Tarjeta Débito",
                "Crédito"
            ]
        }

        for forma_pago in datos_forma_pago["forma_pago"]:
            registro_forma_pago = FormaPago(
                nombre = forma_pago
            )
            registro_forma_pago.save()


    #DATOS GENERALES DE TIPO PAGO
    registro_metodo_pago = MetodoPago.objects.all()
    if not registro_metodo_pago:
        datos_metodo_pago = {
            "metodo_pago": [
                "Pago en una sola exhibición",
                "Pago en parcialidades o diferido"
            ]
        }

        for metodo_pago in datos_metodo_pago["metodo_pago"]:
            registro_metodo_pago = MetodoPago(
                nombre = metodo_pago
            )
            registro_metodo_pago.save()


    #DATOS GENERALES DE CATEGORIA DE PRODUCTO
    categoria_producto = CategoriaProducto.objects.all()
    if not categoria_producto:
        datos_categorias = {
            "categorias": [
                "Electrónica",
                "Ropa",
                "Alimentos",
                "Artículos para el hogar",
                "Belleza y cuidado personal",
                "Juguetes y juegos",
                "Deportes y fitness",
                "Libros y material educativo",
                "Jardinería y exteriores",
                "Salud y bienestar"
            ]
        }

        for categoria in datos_categorias["categorias"]:
            registro_categoria_producto = CategoriaProducto(
                nombre = categoria
            )
            registro_categoria_producto.save()

    categoria_producto = CategoriaProducto.objects.all()

    #datos generales proveedor:
    registro_proveedor = Proveedor.objects.all()
    if not registro_proveedor:
        registro_proveedor = Proveedor(
            nombre = "ElectroTech S.A. de C.V.",
            rfc = "ETC123456ABC",
            codigo_postal = "06450",
            direccion = "Av. Tecnológico #123",
            telefono = "(55) 1234-5678",
            ciudad = "Ciudad de México",
            estado = "Ciudad de México",
            email = "contacto@electrotech.com",
            contacto = "Juan Pérez",
            web = "www.electrotech.com"
        )
        registro_proveedor.save()


    #datos generales producto:
    registro_producto = Producto.objects.all()
    if not registro_producto:
        registro_proveedor = Proveedor.objects.all().last()

        datos_productos = {
            "productos": [
                {
                "categoria": "Electrónica",
                "nombre": "Smartwatch FitX",
                "descripcion": "Smartwatch con pantalla táctil a color, monitor de ritmo cardíaco y seguimiento de actividad física.",
                "marca": "FitTech",
                "costo": 80,
                "precio_publico": 149,
                "existencias": 100
                },
                {
                "categoria": "Electrónica",
                "nombre": "Auriculares Bluetooth Elite",
                "descripcion": "Auriculares inalámbricos con cancelación de ruido, micrófono integrado y estuche de carga.",
                "marca": "SonicX",
                "costo": 50,
                "precio_publico": 99,
                "existencias": 150
                },
                {
                "categoria": "Ropa",
                "nombre": "Camisa Oxford Classic",
                "descripcion": "Camisa de algodón con diseño clásico, cuello abotonado y puños ajustables.",
                "marca": "ModaVest",
                "costo": 30,
                "precio_publico": 59.99,
                "existencias": 200
                },
                {
                "categoria": "Ropa",
                "nombre": "Jeans Slim Fit Essential",
                "descripcion": "Jeans de mezclilla con corte slim fit, diseño moderno y lavado vintage.",
                "marca": "DenimStyle",
                "costo": 35,
                "precio_publico": 69.99,
                "existencias": 150
                },
                {
                "categoria": "Alimentos",
                "nombre": "Café Orgánico Premium",
                "descripcion": "Café orgánico de alta calidad, tostado medio, aroma intenso y sabor suave.",
                "marca": "BioCafé",
                "costo": 10,
                "precio_publico": 19.99,
                "existencias": 300
                },
                {
                "categoria": "Alimentos",
                "nombre": "Salsa Picante Artesanal",
                "descripcion": "Salsa picante elaborada con chiles selectos, sin conservantes ni colorantes artificiales.",
                "marca": "SaborMex",
                "costo": 5,
                "precio_publico": 9.99,
                "existencias": 250
                },
                {
                "categoria": "Artículos para el hogar",
                "nombre": "Juego de Toallas Luxury",
                "descripcion": "Juego de toallas de algodón egipcio, suaves al tacto y absorbentes, incluye toalla de baño y de mano.",
                "marca": "CottonComfort",
                "costo": 20,
                "precio_publico": 39.99,
                "existencias": 120
                },
                {
                "categoria": "Artículos para el hogar",
                "nombre": "Set de Ollas y Sartenes Premium",
                "descripcion": "Set de ollas y sartenes de acero inoxidable de alta calidad, antiadherentes y aptos para todo tipo de cocinas.",
                "marca": "MasterChef",
                "costo": 100,
                "precio_publico": 199.99,
                "existencias": 80
                },
                {
                "categoria": "Belleza y cuidado personal",
                "nombre": "Crema Hidratante Antiedad",
                "descripcion": "Crema hidratante facial con efecto antiedad, fórmula ligera, no grasa y de rápida absorción.",
                "marca": "YouthfulGlow",
                "costo": 25,
                "precio_publico": 49.99,
                "existencias": 150
                },
                {
                "categoria": "Belleza y cuidado personal",
                "nombre": "Set de Brochas Profesionales",
                "descripcion": "Set de brochas profesionales para maquillaje, cerdas suaves y resistentes, incluye estuche de viaje.",
                "marca": "GlamBrush",
                "costo": 15,
                "precio_publico": 29.99,
                "existencias": 200
                },
                {
                "categoria": "Juguetes y juegos",
                "nombre": "Rompecabezas 3D Estrella del Espacio",
                "descripcion": "Rompecabezas 3D de 1000 piezas, diseño de estrella del espacio, desafío divertido para toda la familia.",
                "marca": "PuzzleMaster",
                "costo": 20,
                "precio_publico": 39.99,
                "existencias": 100
                },
                {
                "categoria": "Juguetes y juegos",
                "nombre": "Set de Construcción Bloques Creativos",
                "descripcion": "Set de construcción con bloques creativos, fomenta la imaginación y la destreza manual en los niños.",
                "marca": "BuildFun",
                "costo": 30,
                "precio_publico": 59.99,
                "existencias": 80
                },
                {
                "categoria": "Deportes y fitness",
                "nombre": "Balón de Fútbol Profesional",
                "descripcion": "Balón de fútbol profesional con diseño clásico, cosido a mano, ideal para entrenamientos y partidos.",
                "marca": "SoccerPro",
                "costo": 25,
                "precio_publico": 49.99,
                "existencias": 200
                },
                {
                "categoria": "Deportes y fitness",
                "nombre": "Set de Pesas y Barra Olímpica",
                "descripcion": "Set de pesas y barra olímpica de alta calidad, perfecto para entrenamientos de fuerza en casa o en el gimnasio.",
                "marca": "IronGym",
                "costo": 150,
                "precio_publico": 299.99,
                "existencias": 120
                },
                {
                "categoria": "Libros y material educativo",
                "nombre": "Libro de Cocina Gourmet",
                "descripcion": "Libro de cocina con recetas gourmet, ilustraciones a color y consejos de expertos en gastronomía.",
                "marca": "ChefBook",
                "costo": 15,
                "precio_publico": 29.99,
                "existencias": 150
                },
                {
                "categoria": "Libros y material educativo",
                "nombre": "Set de Pinturas y Lienzos Artísticos",
                "descripcion": "Set de pinturas acrílicas y lienzos artísticos, perfecto para artistas principiantes y aficionados.",
                "marca": "ArtCreativity",
                "costo": 20,
                "precio_publico": 39.99,
                "existencias": 100
                },
                {
                "categoria": "Jardinería y exteriores",
                "nombre": "Plantas Suculentas Variadas",
                "descripcion": "Set de plantas suculentas variadas, fáciles de cuidar y perfectas para decorar interiores y exteriores.",
                "marca": "GreenThumb",
                "costo": 8,
                "precio_publico": 16.99,
                "existencias": 300
                },
                {
                "categoria": "Jardinería y exteriores",
                "nombre": "Set de Herramientas de Jardinería",
                "descripcion": "Set de herramientas de jardinería de alta calidad, incluye pala, rastrillo, tijeras de podar y más.",
                "marca": "GardenPro",
                "costo": 30,
                "precio_publico": 59.99,
                "existencias": 200
                },
                {
                "categoria": "Salud y bienestar",
                "nombre": "Masajeador Shiatsu Premium",
                "descripcion": "Masajeador Shiatsu para cuello y espalda, con función de calor y ajuste de intensidad, alivia el estrés y la tensión muscular.",
                "marca": "RelaxZone",
                "costo": 40,
                "precio_publico": 79.99,
                "existencias": 150
                },
                {
                "categoria": "Salud y bienestar",
                "nombre": "Set de Velas Aromáticas Relajantes",
                "descripcion": "Set de velas aromáticas con fragancias relajantes, perfectas para crear un ambiente tranquilo y acogedor en casa.",
                "marca": "ZenCandle",
                "costo": 20,
                "precio_publico": 39.99,
                "existencias": 120
                }
            ]
            }

        for producto in datos_productos["productos"]:            
            registro_producto = Producto(
                proveedor = registro_proveedor,
                categoria = CategoriaProducto.objects.get(nombre = producto["categoria"]),
                nombre = producto["nombre"],
                descripcion = producto["nombre"],
                marca = producto["marca"],
                costo = producto["costo"],
                precio_publico = producto["precio_publico"],
                existencias = producto["existencias"]
                
            )
            registro_producto.save()

    return redirect('index')


@login_required
def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)
