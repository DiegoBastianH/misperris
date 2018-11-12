# Generated by Django 2.1.2 on 2018-10-26 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='formulariopersona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CorreoElectronico', models.CharField(max_length=40)),
                ('Rut', models.CharField(max_length=9)),
                ('NombreCompleto', models.CharField(max_length=50)),
                ('FechaNacimiento', models.DateField()),
                ('Telefono', models.CharField(max_length=8)),
                ('Direccion', models.CharField(max_length=8)),
            ],
        ),
    ]
