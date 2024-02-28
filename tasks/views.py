from django.shortcuts import render


# Create your views here.
def task_manager(request):
    return render(request, "tasks.html")