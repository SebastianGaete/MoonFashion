# Generated by Django 4.2.4 on 2023-08-08 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mitienda', '0011_remove_comentario_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interesado',
            name='apellido',
            field=models.CharField(max_length=50, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='interesado',
            name='nombre',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='interesado',
            name='telefono',
            field=models.CharField(max_length=50, verbose_name='Número de teléfono'),
        ),
        migrations.AlterField(
            model_name='interesado',
            name='tipo_entrega',
            field=models.CharField(max_length=60, verbose_name='Tipo de entrega'),
        ),
    ]
