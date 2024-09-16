# Generated by Django 5.1.1 on 2024-09-14 15:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0002_remove_customar_customar_type_customar_customer_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='customar_ditail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=10, max_digits=100)),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.customar')),
            ],
        ),
    ]
