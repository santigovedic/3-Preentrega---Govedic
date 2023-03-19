from django import forms


class ProdForm(forms.Form):  # Formulario de carga de los productos.

    tipo = forms.CharField(min_length=3, max_length=15)
    marca = forms.CharField(min_length=3, max_length=15,)
    stock = forms.IntegerField(min_value=1)  # Cuanto stock ingresa a la base de datos con la carga.


class BusquedaProd(forms.Form):  # Formulario de búsqueda de los productos

    tipo = forms.CharField(min_length=3, max_length=15)
    # Va a buscar por tipo de bebida que tengamos, y va a mostrar que marcas hay (cerveza, vino, etc).


class ClienteForm(forms.Form):  # Formulario de carga de los clientes.
    nombre = forms.CharField(min_length=3, max_length=30)
    apellido = forms.CharField(min_length=3, max_length=30)
    email = forms.EmailField()
    edad = forms.IntegerField(min_value=18)


class ProvForm(forms.Form):  # Formulario de carga de los proveedores.
    razon_social = forms.CharField(min_length=3, max_length=30)
    email = forms.EmailField()
    telefono = forms.IntegerField(min_value=111111)
