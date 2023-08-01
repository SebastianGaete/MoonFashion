# Generated by Django 4.2.1 on 2023-08-01 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0007_rename_nombres_categoria_nombre_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='id',
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='productos', verbose_name='Imagen'),
        ),
    ]
