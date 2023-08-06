from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_shippingmethods, name='shippingmethods'),
    path('add/', views.add_shippingmethod, name='add_shippingmethod'),
    path('edit/<int:shippingmethod_id>/', views.edit_shippingmethod, name='edit_shippingmethod'),
    path('delete/<int:shippingmethod_id>/', views.delete_shippingmethod, name='delete_shippingmethod'),
    path('shippingcosts/', views.all_shippingcosts, name='shippingcosts'),
    path('shippingcosts/add/', views.add_shippingcost, name='add_shippingcost'),
    path('shippingcosts/edit/<int:shippingcost_id>/', views.edit_shippingcost, name='edit_shippingcost'),
    path('shippingcosts/delete/<int:shippingcost_id>/', views.delete_shippingcost, name='delete_shippingcost'),
]
