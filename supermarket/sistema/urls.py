from django.urls import path

from .views import *

app_name = 'sistema'
urlpatterns = [
    path("", index, name="index"),
    path("registro/cliente/", registroCliente, name="registro_cliente"),
    path("agregar/carrito/", agregarCarrito, name="agregar_carrito"),    
    path("carrito/", carrito, name="carrito"),    
    path("carrito/cancelar/", cancelarCarrito, name="cancelar_carrito"),    
    path("mis_compras/", verMisCompras, name="mis_compras"),    
    path("facturas/", verFacturas, name="facturas"),    
    path("deudas/", verDeudas, name="deudas"),    

]