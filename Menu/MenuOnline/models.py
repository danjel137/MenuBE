import uuid

from django.db import models


# Create your models here.
class Menu(models.Model):
    id = models.AutoField(primary_key=True)  # This will create an auto-incrementing ID field
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "menu_offered"

    def __str__(self):
        return self.name


class Customer(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    idCard = models.CharField(max_length=100, null=True)  # This will create an auto-incrementing ID field
    name = models.CharField(max_length=50,null=True)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postalCode = models.CharField(max_length=50)

    class Meta:
        db_table = "customer"

    def __str__(self):
        return self.name


class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    items = models.JSONField()
    amount = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = "bill"

    def __str__(self):
        return self.id
