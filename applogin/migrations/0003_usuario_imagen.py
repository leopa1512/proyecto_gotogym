# Generated by Django 3.2.8 on 2021-10-25 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applogin', '0002_auto_20211024_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagen_user', verbose_name='imagen usuario'),
        ),
    ]
