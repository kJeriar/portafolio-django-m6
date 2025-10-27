from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_proyectos, name="lista_proyectos"),
     path("proyecto/<path:titulo_proyecto>/", views.detalle_proyecto, name="detalle_proyecto"),
]

