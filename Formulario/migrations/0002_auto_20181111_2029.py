# Generated by Django 2.1.2 on 2018-11-11 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Formulario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formularios',
            name='image',
            field=models.FileField(upload_to='media'),
        ),
    ]