from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Automovil(models.Model):
    patente = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField(verbose_name='año')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente

    class Meta:
        verbose_name = "Automovil"
        verbose_name_plural = "Automoviles"

     
