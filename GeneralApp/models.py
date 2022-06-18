from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombreCompleto = models.CharField(max_length=40)
    fechaDeNacimiento = models.DateField()
    email = models.EmailField()
    direccion = models.CharField(max_length=40)
    telefono = models.IntegerField()
    def __str__(self) -> str:
        return self.nombreCompleto + ' '+ str(self.fechaDeNacimiento)

class Asociado(models.Model):
    nombreCompleto = models.CharField(max_length=40)
    fechaDeNacimiento = models.DateField()
    email = models.EmailField()
    direccion = models.CharField(max_length=40)
    telefono = models.IntegerField()
    modeloCarroCamioneta = models.CharField(max_length=40)
    def __str__(self) -> str:
        return self.nombreCompleto + ' '+ self.modeloCarroCamioneta

class Proveedor(models.Model):
    nombreCompania = models.CharField(max_length=40)
    nit = models.IntegerField()
    direccion = models.CharField(max_length=40)
    telefono = models.IntegerField()
    servico = models.CharField(max_length=40)
    def __str__(self) -> str:
        return self.nombreCompania + ' '+ self.servico

