from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_product_sizes, name='all_product_sizes'),
    path('add/', views.add_product_size, name='add_product_size'),
    path('edit/<int:product_size_id>/', views.edit_product_size, name='edit_product_size'),
    path('delete/<int:product_size_id>/', views.delete_product_size, name='delete_product_size'),
    path('get-filtered-products/', views.get_filtered_products, name='get_filtered_products'),
    path('get-filtered-sizes/', views.get_filtered_sizes, name='get_filtered_sizes'),
]
