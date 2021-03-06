from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Destinos(models.Model):

    pais = models.CharField(max_length=25)
    ciudad = models.CharField(max_length=25)

    def __str__(self): 
        return f'{self.pais} - {self.ciudad}'

class Alojamientos(models.Model):

    tipo = models.CharField(max_length=25)
    precio = models.FloatField(max_length=20)
    visitantes = models.IntegerField()

    def __str__(self): 
        return f'{self.tipo}-{self.visitantes}-{self.precio}'

class Excursiones(models.Model):

    lugar = models.CharField(max_length=25)
    duracion = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self): 
        return f'{self.lugar}-{self.duracion}-{self.precio}'


class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta avatares media :)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self): 
        return f'Imagen de: {self.user.username}'