from django.shortcuts import render
from tickets.models import Tickets
from django.contrib import messages


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
    get_customer_id = Tickets.objects.filter(customer=request.POST.get("customer"))
    if request.method == "POST":
        new_ticket = Tickets.objects.create(
            subject=request.POST.get("subject"),
            customer=get_customer_id,
            asigned_to=request.POST.get("asigned"),
            agent=request.POST.get("agent"),
            description=request.POST.get("description"),
            priority=request.POST.get("priority"),
            status=request.POST.get("status"),
            ticket_type=request.POST.get("ticketType"),
            chanel=request.POST.get("channel")
        )
        new_ticket.save()
        messages.success(request, "Ticket creado conn exito!, click para ver")

    context = {
        "tickets": tickets
    }
    return render(request, "generate_ticket_form.html", context=context)


# Vista para cerrar un ticket
def close_ticket(request):
    pass
