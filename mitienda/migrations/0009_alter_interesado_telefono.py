# Generated by Django 4.2.3 on 2023-07-24 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mitienda', '0008_delete_poleron'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interesado',
            name='telefono',
            field=models.CharField(verbose_name='Número de teléfono'),
        ),
    ]
