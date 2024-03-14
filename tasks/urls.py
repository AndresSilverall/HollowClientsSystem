from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('delete/<str:pk>', view=views.delete_task, name="delete"),
    path('tasks/', view=views.task_manager, name="tasks"),
    path('add/', view=views.add_task, name="add"),
    path('update/<str:pk>', view=views.update_task, name="update"),
   


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)