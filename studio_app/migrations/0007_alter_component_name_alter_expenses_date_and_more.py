# Generated by Django 4.2.3 on 2023-11-05 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio_app', '0006_rename_value_component_unit_remove_component_lab_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 11, 5, 15, 12, 27, 516287)),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 11, 5, 15, 12, 27, 515278)),
        ),
        migrations.AlterField(
            model_name='purchases',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 11, 5, 15, 12, 27, 515640)),
        ),
    ]