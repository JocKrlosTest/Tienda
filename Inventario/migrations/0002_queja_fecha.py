# Generated by Django 4.1.3 on 2022-12-08 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='queja',
            name='fecha',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
