from django.contrib import admin
from django.utils.html import format_html

from .models import Proyecto, ProyectoImagen


class ProyectoImagenInline(admin.TabularInline):
	model = ProyectoImagen
	extra = 1
	readonly_fields = ('preview_imagen',)
	fields = ('imagen', 'preview_imagen')

	def preview_imagen(self, obj):
		if obj.imagen and obj.pk:
			return format_html(
				'<img src="{}" style="max-height: 120px; border-radius: 6px;" />',
				obj.imagen.url,
			)
		return 'Sin imagen'

	preview_imagen.short_description = 'Vista previa'


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'fecha')
	search_fields = ('nombre',)
	inlines = [ProyectoImagenInline]
