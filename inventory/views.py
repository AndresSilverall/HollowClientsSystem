from django.shortcuts import render

# Vista del control de inventario
def inventory(request):
    return render(request, "inventory.html")