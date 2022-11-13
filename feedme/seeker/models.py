from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Lugar(models.Model):
    nombre = models.CharField(max_length=200,null=True)
    direccion = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.nombre

class Edificio_Piso(models.Model):
    nombre=models.ForeignKey(Lugar,on_delete=models.CASCADE)
    nombre_edificio=models.CharField(max_length=200,null=True)
    piso=models.CharField(max_length=200,null=True)
    instrucciones_salida= models.TextField(blank=True);

    def __str__(self):
        return str(self.nombre)+","+self.nombre_edificio+","+str(self.piso)
    def get_instrucciones_salida(self):
        return self.instrucciones_salida.split("\n")
class Alimento(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    calorias = models.FloatField(null=True)
    grasas = models.FloatField(null=True)
    proteina = models.FloatField(null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre


class Receta(models.Model):
    alimento = models.ManyToManyField(Alimento)
    nombre = models.CharField(max_length=200, null=True)
    preparacion = models.TextField(null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre

    def url_readable_title(self):
        return self.nombre.replace(' ', '-')


class Ingrediente(models.Model):
    receta = models.ManyToManyField(Receta)
    alimento = models.ManyToManyField(Alimento)
    porcion = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.alimento)+self.porcion



class Usuario(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    recetas = models.ManyToManyField(Receta)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    def __user__(self):
        return self.user


class Tutor(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    usuarios = models.ManyToManyField(Usuario)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)

    def __user__(self):
        return self.user
