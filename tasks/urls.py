from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('tasks/', view=views.task_manager, name="tasks"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)