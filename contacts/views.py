from django.shortcuts import render


# Vista para gestionar los contactos y crear campañas de marketing.
def contact_management(request):
    return render(request, "contacts.html")
