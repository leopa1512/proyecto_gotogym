# Generated by Django 3.2.8 on 2021-12-05 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcatalogo', '0004_descuento_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imag_prod',
            field=models.ImageField(null=True, upload_to='imagen_user', verbose_name='imagen usuario'),
        ),
    ]
