from django.contrib import admin
from django import forms
from django.utils.html import format_html

from .models import Proyecto, ProyectoImagen

admin.site.site_url = 'https://refrigeracionroberto.com/'


class ProyectoForm(forms.ModelForm):
	class Meta:
		model = Proyecto
		fields = '__all__'
		widgets = {
			'descripcion': forms.Textarea(attrs={
				'style': 'width:100%; max-width:100%; box-sizing:border-box; resize:vertical;',
				'rows': '6',
			}),
		}


class ProyectoImagenInline(admin.TabularInline):
	model = ProyectoImagen
	extra = 1
	readonly_fields = ('preview_imagen',)
	fields = ('imagen', 'preview_imagen')

	class Media:
		css = {'all': ('admin/css/imagen_inline.css',)}
		js = ('admin/js/imagen_preview.js',)

	def preview_imagen(self, obj):
		if obj.imagen and obj.pk:
			return format_html(
				'<div class="preview-container">'
				'<img class="preview-img" src="{}"/>'
				'</div>',
				obj.imagen.url,
			)
		return format_html(
			'<div class="preview-container">'
			'<img class="preview-img" src="" style="display:none;"/>'
			'<span class="preview-placeholder">Sin imagen</span>'
			'</div>'
		)

	preview_imagen.short_description = 'Vista previa'


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
	form = ProyectoForm
	list_display = ('nombre', 'fecha')
	search_fields = ('nombre',)
	inlines = [ProyectoImagenInline]
