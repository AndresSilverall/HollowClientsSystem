from django.shortcuts import render
from tickets.models import Tickets


# Vista para la gestion de tickets
def tickets_management(request):
    tickets = Tickets.objects.all()

    # Total de tickets
    all_tickets_created = Tickets.objects.count()

    # Tickets abiertos
    open_tickets = Tickets.objects.filter(status="Abierto").count() 

    # Tickets abiertos
    closed_tickets = Tickets.objects.filter(status="Cerrado").count() 

    context = {
        "tickets": tickets,
        "all_tickets_created": all_tickets_created,
        "open_tickets": open_tickets,
        "closed_tickets": closed_tickets
    }

    return render(request, "tickets.html", context=context)


# Vista para generar un nuevo ticket
def generate_ticket_form(request):
    tickets = Tickets.objects.all()
    context = {
        "tickets": tickets
    }
    return render(request, "generate_ticket_form.html", context=context)


# Vista para cerrar un ticket
def close_ticket(request):
    pass
