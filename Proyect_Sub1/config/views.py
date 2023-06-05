from django.http import HttpResponse
from django.shortcuts import render
"""
from django.contrib import admin
from . import models
admin.site.register(models.pais)
admin.site.register(models.cliente)
"""
#from django.template import Context, Template
def saludo(request):
    return HttpResponse("Hola Django - Coder")

def nombre(request, nombre:str, apellido:str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"{apellido},{nombre}")


"""
def probando_template(request):
    mi_html = open("./templates/template1.html",encoding="utf-8")
    mi_template = Template(mi_html.read())
    mi_html.close()
    nombre = "Louis"
    apellido = "Van Beethoven"
    datos = {"nombre": nombre, "apellido":apellido}
    mi_contexto = Context(datos)
    mi_documento = mi_template.render(mi_contexto)
    return HttpResponse(mi_documento)
"""
def probando_templates_render(request):
    nombre = "louis"
    apellido = "van Beethoven"
    datos = {"nombre": nombre, "apellido" : apellido}
    return render(request, "template1.html", context=datos)
def probando_template2(request):
    lista_de_notas = [2,2,3,7,5]
    context = {"notas": lista_de_notas}
    return render(request, "template2.html", context=lista_de_notas)