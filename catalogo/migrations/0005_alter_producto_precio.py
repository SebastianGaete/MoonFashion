# Generated by Django 4.2.1 on 2023-07-30 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0004_categoria_producto_delete_chaqueta_delete_polera_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.CharField(max_length=30, verbose_name='Precio'),
        ),
    ]
