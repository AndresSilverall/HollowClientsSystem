from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path("tickets/", views.tickets_management, name="tickets"),
    path("newTicket/", views.generate_ticket_form, name="generate_ticket"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

