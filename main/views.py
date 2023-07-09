from django.shortcuts import render, redirect, get_object_or_404
from main.models import Producto, Boleta, DetalleBoleta, Usuario, Categoria
from django.contrib.auth import authenticate, login as auth_login


# Página de inicio
def index(request):
    context={}
    return render(request, 'tienda/inicio.html', context)

# Página de admin
def admin_dashboard(request):
    return render(request, 'administrador/dashboard.html')

def tienda(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/tienda.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'tienda/detalle_producto.html', {'producto': producto})


# CRUD Usuarios
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'administrador/lista_usuarios.html', {'usuarios': usuarios})

def crear_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if username and password and email:
            usuario = Usuario(username=username, email=email, first_name=first_name, last_name=last_name)
            usuario.password = password  # Asigna la contraseña directamente al campo "password"
            usuario.save()
            return redirect('lista_usuarios')

    return render(request, 'administrador/crear_usuario.html')

def editar_usuario(request, user_id):
    try:
        usuario = Usuario.objects.get(id=user_id)
        if request.method == 'POST':
            usuario.username = request.POST.get('username')
            usuario.first_name = request.POST.get('first_name')
            usuario.last_name = request.POST.get('last_name')
            usuario.save()
            return redirect('lista_usuarios')
        
        return render(request, 'administrador/editar_usuario.html', {'usuario': usuario})
    except Usuario.DoesNotExist:
        return redirect('lista_usuarios')  # Redirige a la lista de usuarios si el usuario no existe

def eliminar_usuario(request, user_id):
    try:
        usuario = Usuario.objects.get(id=user_id)
        if request.method == 'POST':
            usuario.delete()
            return redirect('lista_usuarios')  # Redirige a la lista de usuarios después de eliminar exitosamente
    except Usuario.DoesNotExist:
        return redirect('lista_usuarios')  # Redirige a la lista de usuarios si el usuario no existe


# CRUD Categorías
def crear_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')

        categoria = Categoria(nombre = nombre) 
        categoria.save()
        return redirect('lista_categorias')
    
    return render(request, 'administrador/crear_categoria.html')
    
def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'administrador/lista_categorias.html', {'categorias': categorias})

def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == 'POST':
        categoria.nombre = request.POST.get('nombre')
        categoria.save()

        return redirect('lista_categorias')

    return render(request, 'administrador/editar_categoria.html', {'categoria': categoria})

def eliminar_categoria(request, categoria_id):
    try:
        categoria = Categoria.objects.get(id=categoria_id)
        if request.method == 'POST':
            categoria.delete()
            return redirect('lista_categorias')  # Redirige a la lista de categorías después de eliminar exitosamente
        return render(request, 'administrador/eliminar_categoria.html', {'categoria': categoria})
    except Categoria.DoesNotExist:
        return redirect('lista_categorias')  # Redirige a la lista de categorías si la categoría no existe

def eliminar_usuario(request, user_id):
    usuario = get_object_or_404(Usuario, id=user_id)

    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')

    return render(request, 'administrador/eliminar_usuario.html', {'usuario': usuario})

# CRUD Productos
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'administrador/lista_productos.html', {'productos': productos})

def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        categoria_id = request.POST.get('categoria')
        
        precio = request.POST.get('precio')
        foto = request.FILES.get('foto')
        id_usuario = request.POST.get('id_usuario')

        categoria = Categoria.objects.get(id=categoria_id)  # Obtiene la instancia de Categoria

        producto = Producto(nombre=nombre, descripcion=descripcion, categoria=categoria, precio=precio, foto=foto, id_usuario=id_usuario)
        producto.save()
        return redirect('lista_productos')  # Redirige a la lista de productos después de guardar exitosamente

    categorias = Categoria.objects.all()
    return render(request, 'administrador/crear_producto.html', {'categorias': categorias})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.precio = request.POST.get('precio')
        producto.descripcion = request.POST.get('descripcion')
        producto.foto = request.FILES.get('foto')
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




def registro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if username and password and email:
            usuario = Usuario(username=username, email=email, first_name=first_name, last_name=last_name)
            usuario.password = password  # Asigna la contraseña directamente al campo "password"
            usuario.save()
            return redirect('login')  # Redirige a la página de inicio de sesión
    
    return render(request, 'tienda/registro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            user = None

        if user is not None and Usuario.password == password:
            # Inicio de sesión exitoso
            # Realizar acciones adicionales si es necesario
            return redirect('inicio')  # Redirige a la página de inicio después del inicio de sesión exitoso

        error_message = 'Correo electrónico o contraseña incorrectos'
    else:
        error_message = None

    return render(request, 'tienda/login.html', {'error_message': error_message})


def inicio(request):
    user_id = request.session.get('user_id')

    if user_id:
        user = Usuario.objects.get(pk=user_id)
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
