from django.shortcuts import render, redirect
from authentication.forms import CreateNewUser, ChangePasswordForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash #keep it the user session active


# Vista del Home Page
def home_page(request):
    return render(request, "base.html")


# Vista de registro de usuario
def user_registration(request):

    form = CreateNewUser()

    if request.method == "POST":
        form = CreateNewUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            messages.success(request, f"Usuario {username} registrado con exito!")
        else:
            messages.error(request, "Error, Datos no coinciden!")

    context = {
        "form": form
    }

    return render(request, "register.html", context=context)


# Vista de login de usuario
def user_login(request):

    form = CreateNewUser()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
        print(request.method)
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


# Vista de reestablecer contraseña
def restart_password(request):
    form = ChangePasswordForm(user=request.user)
    if request.method == "POST":
        form = ChangePasswordForm(user=request.POST, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Contraseña restablecida con exito!")
    
    context = {
        "form": form
    }

    return render(request, "change_password.html", context=context)


# Vista para cerrar la sesion
def user_logout(request):
    return None


# Vista sobre informacion de la App
def about_us(request):
    return render(request, "about_us.html")