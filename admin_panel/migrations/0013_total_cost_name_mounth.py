# Generated by Django 5.1.1 on 2024-09-18 15:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0012_mounth_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='total_cost',
            name='name_mounth',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.mounth_name'),
            preserve_default=False,
        ),
    ]
