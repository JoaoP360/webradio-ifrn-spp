# Generated by Django 5.0.6 on 2024-10-12 04:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='programep',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.program'),
        ),
    ]
