# Generated by Django 4.2.6 on 2023-11-25 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MenuOnline', '0009_customer_idcard_customer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='customer',
        ),
    ]
