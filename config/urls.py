from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include("authentication.urls")),
    path('', include("menu.urls")),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

