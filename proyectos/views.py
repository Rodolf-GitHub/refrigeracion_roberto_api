from django.http import JsonResponse

from .models import Proyecto


def lista_proyectos(request):
	proyectos = Proyecto.objects.prefetch_related('imagenes').all()
	data = []

	for proyecto in proyectos:
		data.append(
			{
				'id': proyecto.id,
				'nombre': proyecto.nombre,
				'descripcion': proyecto.descripcion,
				'fecha': proyecto.fecha,
				'imagenes': [
					request.build_absolute_uri(img.imagen.url)
					for img in proyecto.imagenes.all()
					if img.imagen
				],
			}
		)

	return JsonResponse(data, safe=False)
