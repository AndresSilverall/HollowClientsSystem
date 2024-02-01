from django.urls import path
from authentication.views import example_view


urlpatterns = [
    path('index/', example_view, name="index"),
    
]