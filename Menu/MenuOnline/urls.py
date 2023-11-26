from django.urls import path
from . import views

urlpatterns = [
    path('addMenuItemList/', views.addMenuItemList),
    path('getMenuList/', views.getMenuList),
    path('getCustomerList/', views.getCustomerList),
    path('addCustomer/', views.addCustomer),
    path('addBill/', views.addBill),
]
