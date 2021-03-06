# Generated by Django 3.2.8 on 2021-12-05 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='estado')),
                ('date_crea', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('date_mod', models.DateTimeField(auto_now=True, verbose_name='fecha de modificación')),
                ('user_mod', models.IntegerField(blank=True, null=True, verbose_name='Usuario que modifica')),
                ('descripcion', models.CharField(help_text='Descripción de la categoria', max_length=100, unique=True)),
                ('tipo_plan', models.CharField(max_length=20, verbose_name='tipo facturacion')),
                ('cant_user', models.IntegerField(default=0, verbose_name='cantidad de usuarios')),
                ('preciop', models.FloatField(default=0, verbose_name='precio del plan')),
                ('user_crea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'TipoPlanes',
            },
        ),
    ]
