from django.contrib import admin
from .models import Album, Foto


# Configuración del modelo Albúm.
class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "titulo",
        "descripcion",
        "fecha_creacion",
        "usuario",
    )
    list_editable = ("titulo",)
    list_filter = (
        "id",
        "titulo",
        "descripcion",
        "fecha_creacion",
        "usuario",
    )
    search_fields = (
        "titulo",
        "descripcion",
        "fecha_creacion",
    )
    date_hierarchy = "fecha_creacion"


# Configuración del modelo Foto.
class FotoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "album",
        "imagen",
        "fecha_subida",
    )
    list_editable = ("album",)
    list_filter = ("id", "album", "fecha_subida",)
    search_fields = ("id", "album", "fecha_subida")
    date_hierarchy = "fecha_subida"


# Register your models here.
admin.site.register(Album, AlbumAdmin)
admin.site.register(Foto, FotoAdmin)
