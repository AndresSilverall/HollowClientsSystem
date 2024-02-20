from django.shortcuts import render


# Vistas de autenticacion.
def home_page(request):
    return render(request, "base.html")


def user_registration(request):
    return render(request, "register.html")


def user_login(request):
    return render(request, "login.html")


def user_logout(request):
    return None