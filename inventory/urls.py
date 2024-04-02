from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('inventory/', views.inventory, name="inventory"),
    path('brands/', views.brands, name="brands"),
    path('store/', views.stores, name="stores"),
    path('orders/', views.orders, name="orders"),
    path('category/', views.categories, name="category"),
    path('products/', views.products, name="products"),
    path('addBrand/', views.add_new_brand, name="add_brand"),
    path('deleteBrand/<str:pk>', views.delete_brand, name="delete_brand"),
    path('updateBrand/<str:pk>', views.update_brand, name="update_brand"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)