from django.shortcuts import render
from tasks.models import TasksManagement


# Vista del menu principal
def dashboard(request):
    tasks = TasksManagement.objects.count()
    context = {
        "tasks": tasks
    }
    return render(request, "dashboard.html", context=context)
