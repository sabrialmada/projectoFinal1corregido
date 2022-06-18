from django import forms

class fUsuarioFormulario(forms.Form):
    nombreCompleto = forms.CharField(max_length=40)
    fechaDeNacimiento = forms.DateField()
    email = forms.EmailField()
    direccion = forms.CharField(max_length=40)
    telefono = forms.IntegerField()

class fAsociadoFormulario(forms.Form):
    nombreCompleto = forms.CharField(max_length=40)
    fechaDeNacimiento = forms.DateField()
    email = forms.EmailField()
    direccion = forms.CharField(max_length=40)
    telefono = forms.IntegerField()
    modeloCarroCamioneta = forms.CharField(max_length=40)

class fProveedorFormulario(forms.Form):
    nombreCompania = forms.CharField(max_length=40)
    nit = forms.IntegerField()
    direccion = forms.CharField(max_length=40)
    telefono = forms.IntegerField()
    servico = forms.CharField(max_length=40)