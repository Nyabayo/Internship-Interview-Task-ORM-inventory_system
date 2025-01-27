from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.list_products, name='list_products'),
    path('products/add/', views.add_product, name='add_product'),
    path('products/<int:product_id>/update/', views.update_product, name='update_product'),
    path('products/<int:product_id>/delete/', views.delete_product, name='delete_product'),
]
