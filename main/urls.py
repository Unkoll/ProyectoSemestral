from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('tienda/', views.tienda, name='tienda'),
    path('tienda/producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('administrador/crear_usuario/', views.crear_usuario, name='crear_usuario'),
    path('administrador/productos/', views.lista_productos, name='lista_productos'),
    path('administrador/productos/crear/', views.crear_producto, name='crear_producto'),
    path('administrador/productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'),
    path('administrador/productos/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('login/', views.login_view, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('crear_boleta/', views.crear_boleta, name='crear_boleta'),
    path('ver_boletas/', views.ver_boletas, name='ver_boletas'),
    path('ver_detalle_boleta/<int:boleta_id>/', views.ver_detalle_boleta, name='ver_detalle_boleta'),
]
