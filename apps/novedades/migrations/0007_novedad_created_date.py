# Generated by Django 3.0 on 2021-03-11 19:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('novedades', '0006_auto_20210311_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='novedad',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
