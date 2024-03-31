from django.shortcuts import render


# Vista para la gestion de tickets
def tickets_management(request):
    return render(request, "tickets.html")


# Vista para generar un nuevo ticket
def generate_ticket_form(request):
    return render(request, "ticket_form.html")
