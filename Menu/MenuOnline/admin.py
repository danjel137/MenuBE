from django.contrib import admin
from .models import Menu, Customer, Bill

admin.site.register([Menu,Customer,Bill])
