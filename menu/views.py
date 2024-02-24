from django.shortcuts import render


# Vista del menu principal
def main_menu(request):
    return render(request, "menu.html")
