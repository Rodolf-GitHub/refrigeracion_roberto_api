from django.http import JsonResponse

from .models import Proyecto


def lista_proyectos(request):
	proyectos = Proyecto.objects.all()
	data = []

	for proyecto in proyectos:
		data.append(
			{
				'id': proyecto.id,
				'nombre': proyecto.nombre,
				'descripcion': proyecto.descripcion,
				'fecha': proyecto.fecha,
				'imagen': request.build_absolute_uri(proyecto.imagen.url) if proyecto.imagen else None,
			}
		)

	return JsonResponse(data, safe=False)
