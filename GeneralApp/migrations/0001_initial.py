# Generated by Django 4.0.5 on 2022-06-08 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asociado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCompleto', models.CharField(max_length=40)),
                ('fechaDeNacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
                ('modeloCarroCamioneta', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCompania', models.CharField(max_length=40)),
                ('nit', models.IntegerField()),
                ('direccion', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
                ('servico', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCompleto', models.CharField(max_length=40)),
                ('fechaDeNacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=40)),
                ('telefono', models.IntegerField()),
            ],
        ),
    ]
