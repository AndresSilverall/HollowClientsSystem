from django.shortcuts import render
from tickets.models import Tickets


# Vista para la gestion de tickets
def tickets_management(request):
    tickets = Tickets.objects.all()
    context = {
        "tickets": tickets
    }
    return render(request, "tickets.html", context=context)


# Vista para generar un nuevo ticket
def generate_ticket_form(request):
    return render(request, "generate_ticket_form.html")
