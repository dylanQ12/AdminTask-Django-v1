from django.conf import settings
from django.db import models
import os


# Create your models here.
class Album(models.Model):
    titulo = models.CharField(max_length=200, null=False)
    descripcion = models.TextField(null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    @property
    def ultima_foto(self):
        return self.fotos.order_by("-fecha_subida").first()

class Foto(models.Model):
    album = models.ForeignKey(Album, related_name="fotos", on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="fotos/")
    descripcion = models.TextField(null=True, blank=True)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Foto en {self.album.titulo} - {self.id}"
    
    def save(self, *args, **kwargs):
        if self.pk:  # Si el objeto ya existe, es una actualización
            old_instance = Foto.objects.get(pk=self.pk)
            if old_instance.imagen and self.imagen != old_instance.imagen:
                if os.path.isfile(old_instance.imagen.path):
                    os.remove(old_instance.imagen.path)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.imagen:
            if os.path.isfile(self.imagen.path):
                os.remove(self.imagen.path)
        super().delete(*args, **kwargs)


