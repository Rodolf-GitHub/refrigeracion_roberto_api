from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver


MAX_PROYECTOS = 100
MAX_IMAGE_SIZE_BYTES = 10 * 1024 * 1024


class Proyecto(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='proyectos/')
    descripcion = models.TextField()
    fecha = models.CharField(max_length=20)

    def clean(self):
        super().clean()

        if self.imagen and self.imagen.size > MAX_IMAGE_SIZE_BYTES:
            raise ValidationError({'imagen': 'La imagen no puede superar 10MB.'})

        if not self.pk and Proyecto.objects.count() >= MAX_PROYECTOS:
            raise ValidationError(f'Solo se permiten {MAX_PROYECTOS} proyectos.')

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


@receiver(pre_save, sender=Proyecto)
def eliminar_imagen_anterior_en_actualizacion(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        anterior = Proyecto.objects.get(pk=instance.pk)
    except Proyecto.DoesNotExist:
        return

    imagen_anterior = anterior.imagen
    imagen_nueva = instance.imagen

    if imagen_anterior and imagen_anterior.name and imagen_anterior.name != getattr(imagen_nueva, 'name', None):
        imagen_anterior.delete(save=False)


@receiver(post_delete, sender=Proyecto)
def eliminar_imagen_al_borrar_proyecto(sender, instance, **kwargs):
    if instance.imagen and instance.imagen.name:
        instance.imagen.delete(save=False)


