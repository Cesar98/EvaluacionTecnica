from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Empresas(models.Model): 
    empresa = models.CharField(max_length=20) 

    def __str__(self):
        return self.empresa

class Departamentos(models.Model):
    departamento = models.CharField(max_length=20) 
    empresa = models.ForeignKey(Empresas, default="", on_delete=models.CASCADE)

    def __str__(self):
        return self.departamento

class Empleados(models.Model):
    nombre = models.CharField(max_length=30) 
    fecha_nacimiento = models.DateField()
    email = models.EmailField()
    genero = models.CharField(max_length=1, null=True, blank=True)
    telefono = models.CharField(max_length=30, null=True, blank=True)
    celular = models.CharField(max_length=30, null=True, blank=True) 
    fecha_ingreso = models.DateField()
    departamento = models.ForeignKey(Departamentos, default="", on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

