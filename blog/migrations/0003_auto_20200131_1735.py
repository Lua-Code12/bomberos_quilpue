# Generated by Django 2.2.9 on 2020-01-31 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_automovil_marca'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='automovil',
            options={'verbose_name': 'Automovil', 'verbose_name_plural': 'Automoviles'},
        ),
        migrations.AlterField(
            model_name='automovil',
            name='anio',
            field=models.IntegerField(verbose_name='año'),
        ),
    ]
