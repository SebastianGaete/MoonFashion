# Generated by Django 4.0 on 2023-08-10 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mitienda', '0012_alter_interesado_apellido_alter_interesado_nombre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentacion_prenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='prendas_presentacion')),
            ],
        ),
    ]
