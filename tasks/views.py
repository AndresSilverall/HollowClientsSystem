from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from tasks.models import TasksManagement
from django.contrib import messages


# Vista principal de Tareas
@login_required(redirect_field_name="login")
def task_manager(request):
    
    tasks = TasksManagement.objects.all()

    context = {
        "tasks": tasks
    }
    return render(request, "tasks.html", context=context)


# Vista para eliminar tarea de la base de datos por medio de su ID.
@login_required(redirect_field_name="login")
def delete_task(request, pk): 
    if request.method == "POST":  
        tasks = TasksManagement.objects.get(id=pk)
        tasks.delete()
    return redirect("tasks")


# Vista para agregar una tarea nueva.
@login_required(redirect_field_name="login")
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
@login_required(redirect_field_name="login")
def update_task(request, pk: None):
    if request.method == "POST":
        tasks = TasksManagement.objects.get(id=pk)
        user_data = {
            "title": request.POST.get("taskName"),
            "description": request.POST.get("taskDescription"),
            "priority": request.POST.get("taskPriority"),
            "status": request.POST.get("taskStatus"),
            "due_date": request.POST.get("dueDate"),
        }
        tasks.title = user_data.get("title")
        tasks.description = user_data.get("description")
        tasks.priority = user_data.get("priority")
        tasks.status = user_data.get("status")
        tasks.due_date = user_data.get("due_date")
        tasks.save()
    

    return redirect("tasks")