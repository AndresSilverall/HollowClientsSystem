from django.shortcuts import render, redirect
from tasks.models import TasksManagement


# Vista principal de Tareas
def task_manager(request):
    
    tasks = TasksManagement.objects.all()

    context = {
        "tasks": tasks
    }
    return render(request, "tasks.html", context=context)


# Vista para eliminar tarea de la base de datos.
def delete_task(request, pk: None):    
    tasks = TasksManagement.objects.get(id=pk)
    tasks.delete()
    return redirect("tasks")