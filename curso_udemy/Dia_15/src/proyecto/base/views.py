from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Tarea

class ListaPendientes(ListView):
    model = Tarea
    template_name = "base\\tarea_list.html"
    context_object_name = "tareas"

