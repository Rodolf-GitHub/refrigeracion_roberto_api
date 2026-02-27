from django.urls import path

from .views import lista_proyectos

urlpatterns = [
    path('proyectos/', lista_proyectos, name='lista_proyectos'),
]
