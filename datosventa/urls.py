from django.urls import path
from datosventa.views import inicio, productos, clientes, proveedores, busqueda_productos

urlpatterns = [
    path("", inicio, name='inicio'),
    path('productos/', productos, name='productos'),
    path('busqueda_productos/', busqueda_productos, name='buscarprod'),
    path('clientes/', clientes, name='clientes'),
    path('proveedores/', proveedores, name='proveedores'),
]

