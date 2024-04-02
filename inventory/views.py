from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from inventory.models import (
    Product,
    Category,
    Brand,
    Store,
    Order
)

# -------------------------- Vistas de marcas, tiendas, categorias, productos y ordenes -----------------------


# vista para las tiendas
@login_required(redirect_field_name="login")
def stores(request):
    all_stores = Store.objects.all()
    context = {
        "stores": all_stores
    }
    return render(request, "store.html", context=context)


# Vista para las categorias
@login_required(redirect_field_name="login")
def categories(request):
    category = Category.objects.all()
    context = {
        "categories": category
    }
    return render(request, "category.html", context=context)


# Vista para las marcas
@login_required(redirect_field_name="login")
def brands(request):
    brand = Brand.objects.all()
    context = {
        "brands": brand 
    }
    return render(request, "brands.html", context=context)


# Vista para las ordenes
@login_required(redirect_field_name="login")
def orders(request):
    return render(request, "orders.html")


# Vista para los productos
@login_required(redirect_field_name="login")
def products(request):
    # Todas las tiendas
    stores = Store.objects.all()

    # Todas las categoria
    categories = Category.objects.all()

    # Todas las marcas
    brands = Brand.objects.all()
    context = {
        "stores": stores,
        "categories": categories,
        "brands": brands
    }
    return render(request, "products.html", context=context)


# -------------------------- CRUD para gestionar las marcas  -----------------------

# Vista para agregar unamarca nueva
@login_required(redirect_field_name="login")
def add_new_brand(request):
    if request.method == "POST":
        brand = Brand.objects.create(
            name = request.POST.get("brandName"),
            status = request.POST.get("brandStatus")
        )
        brand.save()
        messages.success(request, "Marca agregada con exito!")
    return redirect("brands")


# Vista para borrar una marca
@login_required(redirect_field_name="login")
def delete_brand(request, pk: None):
    if request.method == "POST":
        brand = Brand.objects.get(id=pk)
        brand.delete()
    return redirect("brands")


# Vista para actualizaruna marca
@login_required(redirect_field_name="login")
def update_brand(request, pk=None):
    if request.method == "POST":
        brand = Brand.objects.get(id=pk)
        brand.name = request.POST.get("brandName")
        brand.status = request.POST.get("brandStatus")
        brand.save()
        messages.success(request, "Marca actualizada con exito!")
    return redirect("brands")


# -------------------------- CRUD para gestionar las tiendas  -----------------------


# Vista para agregar una tienda
@login_required(redirect_field_name="login")
def add_store(request):
    if request.method == "POST":
        store = Store.objects.create(
            name = request.POST.get("storeName"),
            status = request.POST.get("storeStatus")
        )
        store.save()
        messages.success(request, "Tienda agregada con exito!")

    return redirect("stores")


# Vista para agregar una tienda
@login_required(redirect_field_name="login")
def delete_store(request, pk: None):
    if request.method == "POST":
        store = Store.objects.get(id=pk)
        store.delete()
    return redirect("stores")


# Vista para actualizar una tienda
@login_required(redirect_field_name="login")
def update_store(request, pk: None):
    if request.method == "POST":
        store = Store.objects.get(id=pk)
        store.name = request.POST.get("storeName")
        store.status = request.POST.get("storeStatus")
        store.save()

        messages.success(request, "Tienda actualizada con exito!")

    return redirect("stores")


# -------------------------- CRUD para gestionar las categorias  -----------------------

# Vista para agregar una nueva categoria
@login_required(redirect_field_name="login")
def add_category(request):
    if request.method == "POST":
        category = Category.objects.create(
            name=request.POST.get("categoryName"),
            status=request.POST.get("categoryStatus"),
        )
        category.save()
        messages.success(request, "Categoria agregada con exito")
    return redirect("category")


# Vista para actualizar categoria
@login_required(redirect_field_name="login")
def update_category(request, pk: None):
    if request.method == "POST":
        category = Category.objects.get(id=pk)
        category.name = request.POST.get("categoryName")
        category.status= request.POST.get("categoryStatus")
        category.save()
        
        messages.success(request, "Categoria actualizada con exito!")

    return redirect("category")


# Vista para eliminar categoria
@login_required(redirect_field_name="login")
def delete_category(request, pk: None):
    if request.method == "POST":
        category = Category.objects.get(id=pk)
        category.delete()

    return redirect("category")


# Vista para agregar un producto
@login_required(redirect_field_name="login")
def add_product(request):
    if request.method == "POST":
        get_brand_name = Brand.objects.get(name=request.POST.get("brand"))
        get_category_name = Category.objects.get(name=request.POST.get("categoryName"))
        get_store_name = Store.objects.get(name=request.POST.get("store"))

        new_product = Product.objects.create(
            name = request.POST.get("productName"),
            price = int(request.POST.get("price")),
            quantity = request.POST.get("quantity"),
            description = request.POST.get("description"),
            brands = get_brand_name,
            category = get_category_name,
            store = get_store_name
        )
        new_product.save()

        messages.success(request, "Producto agregado con exito!")

    return redirect("products")


