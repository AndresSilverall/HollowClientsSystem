from django.shortcuts import render
from contacts.models import CustomersManagement


# Vista para gestionar los contactos y crear campañas de marketing.
def contact_management(request):
    customers = CustomersManagement.objects.all()
    context = {
        "customers": customers
    }
    return render(request, "contacts.html", context=context)
