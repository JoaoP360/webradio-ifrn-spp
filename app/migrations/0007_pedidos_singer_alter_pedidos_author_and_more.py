# Generated by Django 5.0.6 on 2024-12-10 01:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_rename_solicitationmusic_pedidos'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='singer',
            field=models.CharField(max_length=90, null=True, verbose_name='Cantor'),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='pedidos',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Cadastrado em'),
        ),
    ]
