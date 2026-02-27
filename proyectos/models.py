from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='proyectos/')
    descripcion = models.TextField()
    fecha = models.CharField(max_length=20)


