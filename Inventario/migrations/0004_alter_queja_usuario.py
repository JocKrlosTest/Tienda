# Generated by Django 4.1.3 on 2022-12-08 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0003_venta_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queja',
            name='usuario',
            field=models.CharField(max_length=120),
        ),
    ]