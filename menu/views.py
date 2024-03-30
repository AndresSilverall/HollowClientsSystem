from django.shortcuts import render
from tasks.models import TasksManagement
from contacts.models import CustomersManagement


# Vista del menu principal
def dashboard(request):

    # Estadisticas de la gestion de area
    tasks = TasksManagement.objects.filter(status="en proceso").count()
    tasks_done = TasksManagement.objects.filter(status="Finalizada").count()

    # Estadisticas de la gestion de contactos y campañas de marketing
    customers = CustomersManagement.objects.count()
    active_customers = CustomersManagement.objects.filter(status="Activo").count()
    customers_marketing_campaings = CustomersManagement.objects.filter(campaing="Campaña agregada").count()
    no_marketing_campaings = CustomersManagement.objects.filter(campaing="Sin campaña").count()
    context = {
        "tasks": tasks,
        "is_finished": tasks_done,
        "customers": customers,
        "active_customers": active_customers,
        "customers_campaing": customers_marketing_campaings,
        "no_marketing_campaing": no_marketing_campaings
    }
    return render(request, "dashboard.html", context=context)
