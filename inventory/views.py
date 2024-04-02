from django.shortcuts import render, redirect
from django.contrib import messages
from inventory.models import (
    Product,
    Category,
    Brand,
    Store,
    Order
)


# Vista del control de inventario
def inventory(request):
    return render(request, "inventory.html")


# vista para las tiendas
def stores(request):
    return render(request, "store.html")


# Vista para las categorias
def categories(request):
    return render(request, "category.html")


# Vista para las marcas
def brands(request):
    brand = Brand.objects.all()
    context = {
        "brands": brand 
    }
    return render(request, "brands.html", context=context)


# Vista para las ordenes
def orders(request):
    return render(request, "orders.html")


# Vista para los productos
def products(request):
    return render(request, "products.html")


# -------------------------- CRUD para las diferentes marcas, categorias, tiendas  -----------------------

def add_new_brand(request):
    if request.method == "POST":
        brand = Brand.objects.create(
            name = request.POST.get("brandName"),
            status = request.POST.get("brandStatus")
        )
        brand.save()
        messages.success(request, "Marca agregada con exito!")
    return redirect("brands")


def delete_brand(request, pk: None):
    if request.method == "POST":
        brand = Brand.objects.get(id=pk)
        brand.delete()
    return redirect("brands")


def update_brand(request, pk=None):
    if request.method == "POST":
        brand = Brand.objects.get(id=pk)
        brand.name = request.POST.get("brandName")
        brand.status = request.POST.get("brandStatus")
        brand.save()
        messages.success(request, "Marca actualizada con exito!")
    return redirect("brands")