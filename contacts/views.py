from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from contacts.models import CustomersManagement
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Vista para gestionar los contactos y crear campañas de marketing.
def contact_management(request):
    customers = CustomersManagement.objects.all()
    context = {
        "customers": customers
    }
    return render(request, "contacts.html", context=context)



# Vista para agregar un nuevo cliente
def add_contact(request):
    if request.method == "POST":
        customer = CustomersManagement.objects.create(
            customer=request.POST.get("customer"),
            address=request.POST.get("address"),
            position=request.POST.get("position"),
            interaction=request.POST.get("interaction"),
            preference=request.POST.get("preference"),
            notes=request.POST.get("notes"),
            campaing=request.POST.get("campaing"),
            email=request.POST.get("email"),
            phone_number=request.POST.get("phoneNumber"),
            status=request.POST.get("status")
        )

        customer.save()
        messages.success(request, "Cliente agregado con exito!")

    return redirect("contacts")


# Vista para actulizar un cliente
def update_customer(request, pk:None):
    if request.method == "POST":
        customer = CustomersManagement.objects.get(id=pk)
        customer_info = {
            "customer": request.POST.get("customer"),
            "address": request.POST.get("address"),
            "position": request.POST.get("position"),
            "preference": request.POST.get("preference"),
            "notes": request.POST.get("notes"),
            "campaing": request.POST.get("campaing"),
            "email": request.POST.get("email"),
            "phoneNumber": request.POST.get("phoneNumber"),
            "status": request.POST.get("status")
        }
        customer.title = customer_info.get("customer")
        customer.address = customer_info.get("address")
        customer.position = customer_info.get("position")
        customer.preference = customer_info.get("preference")
        customer.notes = customer_info.get("notes")
        customer.campaing = customer_info.get("campaing")
        customer.email = customer_info.get("email")
        customer.phone_number = customer_info.get("phoneNumber")
        customer.status = customer_info.get("status")

        customer.save()
        messages.success(request, "Cliente actualizado con exito!")

    return redirect("contacts")

# Vista para eliminar un cliente
def delete_customer(request, pk):
    if request.method == "POST":
        customer = CustomersManagement.objects.get(id=pk)
        customer.delete()
    return redirect("contacts")   


# Vista para crear una campaña de marketing a un cliente
def send_marketing_campaing(request, pk: None):
    customer = CustomersManagement.objects.get(id=pk)
    if request.method == "POST":
        subject = request.POST.get("emailSubject")
        email_from = settings.EMAIL_HOST_USER
        recipient = [request.POST.get("emailUser")]
        html_message = render_to_string("social_media_marketing.html")
        plain_message = strip_tags(html_message)

        message = EmailMultiAlternatives(
            subject,
            plain_message,
            email_from,
            recipient
        )

        message.attach_alternative(html_message, "text/html")
        message.send()
        customer.campaing = "Campaña agregada"
        customer.save()
    return redirect("contacts")
