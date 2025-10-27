from django.shortcuts import render
from django.http import Http404


class Proyecto:
    def __init__(self, titulo, descripcion, tecnologias, link_demo=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.tecnologias = tecnologias
        self.link_demo = link_demo



class PortafolioData:
    proyectos = [
        Proyecto(
            titulo="gestor_tareas_django",
            descripcion="App web para administrar desarrollos de proyectos ",
            tecnologias=["Django", "Bootstrap"],
            link_demo="https://github.com/kJeriar/gestor_tareas_django"
        ),
        Proyecto(
            titulo="IPCHILE",
            descripcion="web instituto profesional de educación",
            tecnologias=["php", "js", "HTML/CSS"],
            link_demo="https://www.ipchile.cl/"
        ),
        Proyecto(
            titulo="Santo Domingo",
            descripcion="web municipio",
            tecnologias=["php", "js", "HTML/CSS"],
            link_demo="https://santodomingo.cl/"
        ),
        Proyecto(
            titulo="Donación Transparente",
            descripcion="Plataforma para trazabilidad de donaciones en la comunidad.",
            tecnologias=["PWA", "JavaScript", "DataViz"],
            link_demo="http://google.com"
        ),
    ]


def lista_proyectos(request):
   
    return render(request, "proyectos/lista.html", {
        "proyectos": PortafolioData.proyectos
    })


def detalle_proyecto(request, titulo_proyecto):
    
    for p in PortafolioData.proyectos:
        if p.titulo == titulo_proyecto:
            return render(request, "proyectos/detalle.html", {"proyecto": p})

   
    raise Http404("Proyecto no encontrado")