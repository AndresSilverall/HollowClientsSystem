from django.shortcuts import render
from tasks.models import TasksManagement


# Vista principal de Tareas
def task_manager(request):
    return render(request, "tasks.html")


# Vista de mostrar todas las tareas almacenadas en la BD
def show_all_tasks(request):

    tasks = TasksManagement.objects.all()

    context = {
        "tasks": tasks
    }
    return render(request, "tasks.html", context=context)