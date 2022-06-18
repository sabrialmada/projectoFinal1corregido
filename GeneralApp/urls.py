from django.urls import path
from GeneralApp import views

urlpatterns = [
    path('', views.principal, name='principalPage'),
    path('usuario/', views.usuario, name='usuariosPage'),
    path('asociado/', views.asociado, name='asociadoPage'),
    path('proveedor/', views.proveedor, name='proveedorPage'),
    path('usuarioFormulario/', views.usuarioFormulario, name='usuarioFormulario'),
    path('asociadoFormulario/', views.asociadoFormulario, name='asociadoFormulario'),
    path('proveedorFormulario/', views.proveedorFormulario, name='proveedorFormulario'),
    path('busquedaUsuario/', views.busquedaUsuario, name='busquedaUsuario'),
    path('resultadoBusquedaUsuario/', views.buscarUsuario, name='resultadoBusquedaUsuario'),
    path('busquedaAsociado/', views.busquedaAsociado, name='busquedaAsociado'),
    path('resultadoBusquedaAsociado/', views.buscarAsociado, name='resultadoBusquedaAsociado'),
    path('busquedaProveedor/', views.busquedaProveedor, name='busquedaProveedor'),
    path('resultadoBusquedaProveedor/', views.buscarProveedor, name='resultadoBusquedaProveedor'),



]