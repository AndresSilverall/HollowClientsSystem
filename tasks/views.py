from django.shortcuts import render, redirect
from tasks.models import TasksManagement
from django.contrib import messages


# Vista principal de Tareas
def task_manager(request):
    
    tasks = TasksManagement.objects.all()

    context = {
        "tasks": tasks
    }
    return render(request, "tasks.html", context=context)


# Vista para eliminar tarea de la base de datos.
def delete_task(request, pk: None):  
    if request.method == "POST":  
        tasks = TasksManagement.objects.get(id=pk)
        tasks.delete()
        messages.success(request, "Tarea eliminada con exito!")
    return redirect("tasks")


# Vista para agregar una tarea nueva.
def add_task(request):
    user_data = {
        "name": request.POST.get("taskName"),
        "description": request.POST.get("taskDescription"),
        "priority": request.POST.get("taskPriority"),
        "status": request.POST.get("taskStatus"),
        "due_date": request.POST.get("dueDate")
    }
    if request.method == "POST":
        tasks = TasksManagement.objects.create(
            title=user_data.get("name"),
            description=user_data.get("description"),
            priority=user_data.get("priority"),
            status=user_data.get("status"),
            due_date=user_data.get("due_date"),
        )

        tasks.save()
        messages.success(request, "Tarea agregada con exito!")
    return redirect("tasks")


#Vista para actualizar una tarea
def update_task(request):
    return redirect("tasks")