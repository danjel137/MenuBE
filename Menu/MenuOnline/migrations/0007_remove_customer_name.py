# Generated by Django 4.2.6 on 2023-11-25 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MenuOnline', '0006_alter_customer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
    ]