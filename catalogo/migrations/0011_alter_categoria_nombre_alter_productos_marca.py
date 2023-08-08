# Generated by Django 4.2.4 on 2023-08-08 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0010_productos_delete_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=40, primary_key=True, serialize=False, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='marca',
            field=models.CharField(max_length=50, verbose_name='Marca'),
        ),
    ]
