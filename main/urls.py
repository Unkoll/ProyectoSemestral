from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tienda/', views.tienda, name='tienda'),
    path('tienda/producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    
    path('administrador/', views.admin_dashboard, name='admin_dashboard'),
    
    path('administrador/usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path("administrador/usuarios/crear", views.crear_usuario, name="crear_usuario"),
    path('administrador/usuario/editar/<int:user_id>', views.editar_usuario, name='editar_usuario'),
    path('administrador/usuario/eliminar/<int:user_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    
    path('administrador/categorias/', views.lista_categorias, name='lista_categorias'),
    path('administrador/categorias/crear/', views.crear_categoria, name='crear_categoria'),
    path('administrador/categorias/editar/<int:categoria_id>', views.editar_categoria, name='editar_categoria'),
    path('administrador/categoria/eliminar/<int:categoria_id>', views.eliminar_categoria, name='eliminar_categoria'),
    
    path('administrador/productos/', views.lista_productos, name='lista_productos'),
    path('administrador/productos/crear/', views.crear_producto, name='crear_producto'),
    path('administrador/productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('administrador/productos/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    
    path('login/', views.login, name='login'),
    path("registro/", views.registro, name="registro"),
    
    path('crear_boleta/', views.crear_boleta, name='crear_boleta'),
    path('ver_boletas/', views.ver_boletas, name='ver_boletas'),
    path('ver_detalle_boleta/<int:boleta_id>/', views.ver_detalle_boleta, name='ver_detalle_boleta'),
]
