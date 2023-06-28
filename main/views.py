from django.shortcuts import render, redirect, get_object_or_404
from main.models import Producto, Boleta, DetalleBoleta
from .forms import UserForm, ProductoForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def index(request):
    context={}
    return render(request, 'tienda/inicio.html', context)


def admin_dashboard(request):
    return render(request, 'admin/dashboard.html')


def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/tienda.html', {'productos': productos})


def detalle_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'tienda/detalle_producto.html', {'producto': producto})


def crear_usuario(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = UserForm()

    return render(request, 'administrador/crear_usuario.html', {'form': form})


def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'administrador/lista_productos.html', {'productos': productos})


def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        descripcion = request.POST.get('descripcion')
        foto = request.FILES.get('foto')
        categoria = request.POST.get('categoria')
        id_usuario = request.POST.get('id_usuario')

        producto = Producto(nombre=nombre, precio=precio, descripcion=descripcion, foto=foto, categoria=categoria, id_usuario=id_usuario)
        producto.save()

        return redirect('lista_productos')

    return render(request, 'administrador/crear_producto.html')


def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.precio = request.POST.get('precio')
        producto.descripcion = request.POST.get('descripcion')
        producto.foto = request.FILES.get('foto')
        producto.categoria = request.POST.get('categoria')
        producto.id_usuario = request.POST.get('id_usuario')
        producto.save()

        return redirect('lista_productos')

    return render(request, 'administrador/editar_producto.html', {'producto': producto})


def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')

    return render(request, 'administrador/eliminar_producto.html', {'producto': producto})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            error_message = 'Nombre de usuario o contraseña incorrectos.'
            return render(request, 'tienda/login.html', {'error_message': error_message})

    return render(request, 'tienda/login.html')


def inicio(request):
    user_id = request.session.get('user_id')

    if user_id:
        user = User.objects.get(pk=user_id)
        # Realiza las operaciones necesarias con el objeto User

    # Resto de la lógica de la vista


def crear_boleta(request):
    if request.method == 'POST':
        productos = request.POST.getlist('productos')

        boleta = Boleta.objects.create(id_cliente=request.user.id)

        for producto in productos:
            id_producto = producto['id']
            nombre = producto['nombre']
            precio = producto['precio']
            cantidad = producto['cantidad']
            total = precio * cantidad

            DetalleBoleta.objects.create(
                id_producto=id_producto,
                id_boleta=boleta.id,
                precio=precio,
                cantidad=cantidad,
                total=total
            )

        return redirect('inicio')

    return render(request, 'tienda/inicio.html')


def ver_boletas(request):
    boletas = Boleta.objects.all()
    return render(request, 'tienda/ver_boletas.html', {'boletas': boletas})


def ver_detalle_boleta(request, boleta_id):
    boleta = Boleta.objects.get(id=boleta_id)
    detalles = DetalleBoleta.objects.filter(id_boleta=boleta_id)
    return render(request, 'tienda/ver_detalle_boleta.html', {'boleta': boleta, 'detalles': detalles})
