# Generated by Django 4.2.3 on 2023-07-18 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mitienda', '0006_interesado_mensaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interesado',
            name='tipo_entrega',
            field=models.CharField(max_length=100, verbose_name='Tipo de entrega'),
        ),
    ]