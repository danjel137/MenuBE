# Generated by Django 4.2.6 on 2023-11-25 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MenuOnline', '0004_bill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
