# Generated by Django 4.2.1 on 2023-08-01 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0005_alter_producto_precio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='nombre',
            new_name='nombres',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='categoria',
            new_name='categorias',
        ),
    ]
