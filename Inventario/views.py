from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Producto
from .forms import ProductoForm


def lista_productos(request):

    buscar = request.GET.get('buscar', '')

    qs = Producto.objects.select_related(
        'categoria',
        'marca'
    )

    if buscar:
        qs = qs.filter(
            Q(nombre__icontains=buscar) |
            Q(color__icontains=buscar) |
            Q(descripcion__icontains=buscar) |
            Q(marca__nombre__icontains=buscar) |
            Q(categoria__nombre__icontains=buscar)
        )

    paginator = Paginator(qs, 10)

    productos = paginator.get_page(
        request.GET.get('page')
    )

    return render(
        request,
        'inventario/lista.html',
        {
            'productos': productos,
            'buscar': buscar
        }
    )


def crear_producto(request):

    if request.method == 'POST':

        form = ProductoForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect('inventario:lista')

    else:

        form = ProductoForm()

    return render(
        request,
        'inventario/formulario.html',
        {
            'form': form,
            'titulo': 'Nuevo Producto'
        }
    )


def editar_producto(request, pk):

    producto = get_object_or_404(
        Producto,
        pk=pk
    )

    if request.method == 'POST':

        form = ProductoForm(
            request.POST,
            request.FILES,
            instance=producto
        )

        if form.is_valid():
            form.save()
            return redirect('inventario:lista')

    else:

        form = ProductoForm(
            instance=producto
        )

    return render(
        request,
        'inventario/formulario.html',
        {
            'form': form,
            'titulo': f'Editar {producto.nombre}'
        }
    )


def eliminar_producto(request, pk):

    producto = get_object_or_404(
        Producto,
        pk=pk
    )

    if request.method == 'POST':
        producto.delete()

    return redirect('inventario:lista')