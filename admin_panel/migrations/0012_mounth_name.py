# Generated by Django 5.1.1 on 2024-09-18 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0011_alter_total_cost_bill_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='mounth_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
