from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('contacts/', view=views.contact_management, name="contacts"),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)