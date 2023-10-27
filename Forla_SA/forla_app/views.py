from django.shortcuts import render
from .models import Producto, Cliente, Categoria, Pedido


# Create your views here.

def home(request):
    return render(request, "padre.html")


def producto(request):
    productos = Producto.objects.all()
    return render(request, "productos.html", {"productos": productos})


def nosotros(request):
    return render(request, "nosotros.html")


def productos_formulario(request):
    if request.method == "POST":
        producto = Producto(request.post["nombre"], request.post["descripcion"], request.post["precio"])
        producto.save()
        return render(request, "padre.html")
    return render(request, "productos_formulario.html")
