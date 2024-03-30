from django.shortcuts import render


# Vista para la gestion de tickets
def tickets_management(request):
    return render(request, "tickets.html")
