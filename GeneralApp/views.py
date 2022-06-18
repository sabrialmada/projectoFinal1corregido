from django.shortcuts import render
from GeneralApp import models
from GeneralApp import forms
from django.http import HttpResponse
from .models import Asociado, Proveedor, Usuario
# Create your views here.
def principal(request):
    return render(request, 'GeneralApp/principalPage.html')
def usuario(request):
    return render(request, 'GeneralApp/principalUsuario.html')
def asociado(request):
    return render(request, 'GeneralApp/principalAsociado.html')
def proveedor(request):
    return render(request, 'GeneralApp/principalProveedor.html')

#**VISTA DE FORMULARIOS**#################################################################################

#****VISTA DE FORMULARIO DE USUARIOS****#

def usuarioFormulario(request):

    if request.method == 'POST':
        miFormulario = forms.fUsuarioFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombreCompleto = informacion['nombreCompleto']
        fechaDeNacimiento = informacion['fechaDeNacimiento']
        email = informacion['email']
        direccion = informacion['direccion']
        telefono = informacion['telefono']
        usuario = models.Usuario(nombreCompleto=nombreCompleto, fechaDeNacimiento=fechaDeNacimiento, email=email,direccion=direccion, telefono=telefono)
        usuario.save()
        return render(request, 'GeneralApp/principalPage.html')
    else:
        miFormulario = forms.fUsuarioFormulario()

    return render(request, 'GeneralApp/usuarioFormulario.html', {'miFormulario': miFormulario})

def asociadoFormulario(request):

    if request.method == 'POST':
        miFormulario = forms.fAsociadoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombreCompleto = informacion['nombreCompleto']
        fechaDeNacimiento = informacion['fechaDeNacimiento']
        email = informacion['email']
        direccion = informacion['direccion']
        telefono = informacion['telefono']
        modeloCarroCamioneta = informacion['modeloCarroCamioneta']
        asociado = models.Asociado(nombreCompleto=nombreCompleto, fechaDeNacimiento=fechaDeNacimiento, email=email,direccion=direccion, telefono=telefono, modeloCarroCamioneta = modeloCarroCamioneta)
        asociado.save()
        return render(request, 'GeneralApp/principalPage.html')
    else:
        miFormulario = forms.fAsociadoFormulario()

    return render(request, 'GeneralApp/asociadoFormulario.html', {'miFormulario': miFormulario})

def proveedorFormulario(request):

    if request.method == 'POST':
        miFormulario = forms.fProveedorFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
        nombreCompania = informacion['nombreCompania']
        nit = informacion['nit']
        direccion = informacion['direccion']
        telefono = informacion['telefono']
        servico = informacion['servico']
        proveedor = models.Proveedor(nombreCompania=nombreCompania, nit=nit,direccion=direccion, telefono=telefono, servico=servico)
        proveedor.save()
        return render(request, 'GeneralApp/principalPage.html')
    else:
        miFormulario = forms.fProveedorFormulario()

    return render(request, 'GeneralApp/proveedorFormulario.html', {'miFormulario': miFormulario})

#****VISTA DE BUSQUEDA DE USUARIO!****#
def busquedaUsuario(request):
    
    return render(request, 'GeneralApp/busquedaUsuario.html')

def buscarUsuario(request):
    if request.GET['usuario']:
        usuario = request.GET['usuario']    
        buscar = Usuario.objects.filter(nombreCompleto=usuario).distinct()
        return render(request, 'GeneralApp/resultadoBusquedaUsuario.html',{'buscar':buscar, 'usuario':usuario})
    else:
        respuesta = "No enviaste datos "
        return HttpResponse(respuesta)
#****VISTA DE BUSQUEDA DE ASOCIADO!****#
def busquedaAsociado(request):
    
    return render(request, 'GeneralApp/busquedaAsociado.html')

def buscarAsociado(request):
    if request.GET['asociado']:
        asociado = request.GET['asociado']    
        buscar = Asociado.objects.filter(nombreCompleto=asociado).distinct()
        return render(request, 'GeneralApp/resultadoBusquedaAsociado.html',{'buscar':buscar, 'asociado':asociado})
    else:
        respuesta = "No enviaste datos "
        return HttpResponse(respuesta)

#****VISTA DE BUSQUEDA DE proveedor!****#

def busquedaProveedor(request):
    
    return render(request, 'GeneralApp/busquedaProveedor.html')

def buscarProveedor(request):
    if request.GET['proveedor']:
        proveedor = request.GET['proveedor']    
        buscar = Proveedor.objects.filter(nombreCompania=proveedor).distinct()
        return render(request, 'GeneralApp/resultadoBusquedaProveedor.html',{'buscar':buscar, 'proveedor':proveedor})
    else:
        respuesta = "No enviaste datos "
        return HttpResponse(respuesta)

    