# Generated by Django 3.2.8 on 2021-11-22 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applogin', '0004_alter_usuario_dni'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cod_postal',
            field=models.CharField(blank=True, max_length=10, verbose_name='codigo postal'),
        ),
    ]