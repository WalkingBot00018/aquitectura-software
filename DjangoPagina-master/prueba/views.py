from django.http import HttpResponse
import datetime
from django.template import Template  

def saludo(request):
    doc_externo=open("C:/Users/Aprendiz/prueba/prueba/plantillas/plantilla.html")

    plt=Template(doc_externo.read())

def fecha(request):
    fechita=datetime.datetime.now()
    documento="<html><h1>Fecha de hoy %s </h1></html>" %fechita

    return HttpResponse(documento)
   
def calculandoEdad(request, agno):
    edadActual=20
    periodo=agno-2003
    edadFutura=edadActual+periodo
    documento="<html><h2>En el año %s tendras %s años " %(agno, edadFutura)

    return HttpResponse(documento)