from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Q
from django.contrib import messages

# Create your views here.

layout = """
    <h1> Proyecto Web (LP3) | Flor Cerdán </h1>
    <hr/>
    <ul>
        <li><a href="/inicio">Cursos</a></li>
        <li><a href="/noticias">crear curso</a></li>
        <li><a href="/contacto">carreras</a></li>
        <li><a href="/ayuda">crear carrera</a></li>
    </ul>
    <hr/>
"""
def index(request):
    cursos = [
                    'LP3',
                    'REDES',
                    'FISICA',
                    'ESTADÏSTICA',
                    'BASE DE DATOS']

    return render(request , 'index.html',{
        'code': 'Inicio',
        'mensaje':'Proyecto Web con Django',
        'cursos': cursos
    })

def crear_tabla(request,code,name,hour,credits,state):
    course = Course(
        code = code,
        name = name,
        hour = hour,
        credits = credits,
        state = state
    )
    course.save()
    return HttpResponse(f"Course creado: {course.code} - {course.name}")

def listar_tabla(request):
    courses = Course.objects.all()
    return render(request, 'listar_tabla.html',{
           'courses':courses,
            'code': 'Listado de tabla course'
    })

def crear_tabla(career,name,shortname,image,state):
    career = career(
        name = name;
        shortname = shortname,
        image = image,
        state = state
        )
    return HttpResponse(f"Carrera creada: {career.name} - {career.shortname}")
