# Generated by Django 4.2.3 on 2023-07-21 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_chaqueta_polera'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polera',
            name='imagen',
            field=models.ImageField(upload_to='poleras/images', verbose_name='Imagen'),
        ),
    ]
