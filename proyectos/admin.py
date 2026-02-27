from django.contrib import admin
from django.utils.html import format_html

from .models import Proyecto


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'fecha', 'preview_imagen')
	search_fields = ('nombre',)
	readonly_fields = ('preview_imagen',)
	fields = ('nombre', 'descripcion', 'fecha', 'imagen', 'preview_imagen')

	def preview_imagen(self, obj):
		if obj.imagen:
			return format_html(
				'<img src="{}" style="max-height: 120px; border-radius: 6px;" />',
				obj.imagen.url,
			)
		return 'Sin imagen'

	preview_imagen.short_description = 'Vista previa'
