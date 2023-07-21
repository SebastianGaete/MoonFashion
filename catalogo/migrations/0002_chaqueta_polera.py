# Generated by Django 4.2.3 on 2023-07-21 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chaqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=200, verbose_name='Marca')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('talla', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('EG', 'EG')], max_length=2, verbose_name='Tallas')),
                ('precio', models.CharField(max_length=20, verbose_name='Precio')),
                ('stock', models.IntegerField(default=1, verbose_name='Stock')),
                ('imagen', models.ImageField(upload_to='chaquetas/images', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Chaquetas',
            },
        ),
        migrations.CreateModel(
            name='Polera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=200, verbose_name='Marca')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('talla', models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('EG', 'EG')], max_length=2, verbose_name='Tallas')),
                ('precio', models.CharField(max_length=20, verbose_name='Precio')),
                ('stock', models.IntegerField(default=1, verbose_name='Stock')),
                ('imagen', models.ImageField(upload_to='chaquetas/images', verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Poleras',
            },
        ),
    ]