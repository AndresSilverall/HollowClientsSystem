from django.shortcuts import render, redirect
from authentication.forms import CreateNewUser
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Vistas de autenticacion.
def home_page(request):
    return render(request, "base.html")


def user_registration(request):

    form = CreateNewUser()

    if request.method == "POST":
        form = CreateNewUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            messages.success(request, "Usuario registrado con exito!")
        else:
            messages.error(request, "Error, Datos no coinciden!")

    context = {
        "form": form
    }

    return render(request, "register.html", context=context)


def user_login(request):

    form = CreateNewUser()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request,"Error, usuario o contraseña incorrecta!")

    context = {
        "form": form
    }

    return render(request, "login.html", context=context)


def about_us(request):
    return render(request, "about_us.html")


def restart_password(request):
    return render(request, "change_password.html")


def user_logout(request):
    return None
