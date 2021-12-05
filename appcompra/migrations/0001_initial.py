# Generated by Django 3.2.8 on 2021-12-05 03:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appcatalogo', '0007_alter_descuento_descripcion'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DescuentoF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='estado')),
                ('date_crea', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('date_mod', models.DateTimeField(auto_now=True, verbose_name='fecha de modificación')),
                ('user_mod', models.IntegerField(blank=True, null=True, verbose_name='Usuario que modifica')),
                ('descripcion', models.CharField(help_text='Descripción del descuento', max_length=100, unique=True)),
                ('cant_desc', models.IntegerField(default=0, verbose_name='cantidad del descuento')),
                ('user_crea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Descuentos',
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True, verbose_name='estado')),
                ('date_crea', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('date_mod', models.DateTimeField(auto_now=True, verbose_name='fecha de modificación')),
                ('user_mod', models.IntegerField(blank=True, null=True, verbose_name='Usuario que modifica')),
                ('cod_factura', models.CharField(max_length=50, unique=True)),
                ('tipo_factura', models.CharField(max_length=20, verbose_name='tipo facturacion')),
                ('dni', models.IntegerField(blank=True, null=True, verbose_name='numero identificacion')),
                ('direccion', models.CharField(blank=True, max_length=60, verbose_name='direccion')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='direccion email')),
                ('num_telf', models.CharField(blank=True, max_length=20, verbose_name='numero telefono')),
                ('num_cell', models.CharField(blank=True, max_length=20, verbose_name='numero celular')),
                ('descripcion', models.CharField(max_length=200, verbose_name='descripción producto')),
                ('Sub_total', models.IntegerField(default=0, verbose_name='sun total')),
                ('impuesto', models.IntegerField(default=0, verbose_name='impuesto')),
                ('total_pagar', models.IntegerField(default=0, verbose_name='total pagar')),
                ('plan_contrato', models.IntegerField(blank=True, null=True, verbose_name='plan contratado')),
                ('descuentof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcompra.descuentof')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appcatalogo.producto')),
                ('user_crea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Facturas',
            },
        ),
    ]
