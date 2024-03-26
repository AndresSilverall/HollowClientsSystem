from django.shortcuts import render
from tasks.models import TasksManagement


# Vista del menu principal
def dashboard(request):
    tasks = TasksManagement.objects.filter(status="en proceso").count()
    tasks_done = TasksManagement.objects.filter(status="Finalizada").count()
    context = {
        "tasks": tasks,
        "is_finished": tasks_done
    }
    return render(request, "dashboard.html", context=context)
