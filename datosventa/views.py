from django.shortcuts import render, redirect
from datosventa.forms import ProdForm, ClienteForm, ProvForm, BusquedaProd
from datosventa.models import Producto, Cliente, Proveedor


def inicio(request):  # Pagina de inicio de mi web, donde está el form de búsqueda.
    return render(request, "datosventa/inicio.html")


def productos(request):

    if request.method == "POST":
        mi_form = ProdForm(request.POST)

        if mi_form.is_valid():
            producto_save = Producto()
            producto_save.tipo = mi_form.cleaned_data["tipo"]
            producto_save.marca = mi_form.cleaned_data["marca"]
            producto_save.stock = mi_form.cleaned_data["stock"]
            producto_save.save()

        else:
            mi_form = ProdForm()

    contexto = {"form": ProdForm(), "form_busqueda": BusquedaProd()}
    return render(request, "datosventa/productos.html", context=contexto)


def clientes(request):

    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente_save = Cliente()
            cliente_save.nombre = form.cleaned_data["nombre"]
            cliente_save.apellido = form.cleaned_data["apellido"]
            cliente_save.edad = form.cleaned_data["edad"]
            cliente_save.email = form.cleaned_data["email"]
    else:
        form = ClienteForm()
    contexto = {"formulario": form}
    return render(request, "datosventa/clientes.html", context=contexto)


def proveedores(request):

    if request.method == "POST":
        form = ProvForm(request.POST)
        if form.is_valid():
            prov_save = ProvForm()
            prov_save.razon_social = form.cleaned_data["razon_social"]
            prov_save.telefono = form.cleaned_data["telefono"]
            prov_save.email = form.cleaned_data["email"]
    else:
        form = ProvForm()
    contexto = {"formulario": form}
    return render(request, "datosventa/proveedores.html", context=contexto)


def busqueda_productos(request):
    formulario = BusquedaProd(request.GET)
    if formulario.is_valid():  # Donde ese form sea valido, buscamos la info.
        info = formulario.cleaned_data
        filtro_prod = Producto.objects.filter(tipo__icontains=info["tipo"])
        contexto = {"filtro": filtro_prod}
    return render(request, "datosventa/busqueda_prod.html", context=contexto)








