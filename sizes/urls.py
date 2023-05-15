from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_sizes, name='sizes'),
    path('add/', views.add_size, name='add_size'),
    path('edit/<int:size_id>/', views.edit_size, name='edit_size'),
    path('delete/<int:size_id>/', views.delete_size, name='delete_size'),
    path('assign/<int:size_id>/', views.delete_size, name='assign_size'),
]
