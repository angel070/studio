# Generated by Django 4.2.3 on 2023-10-20 20:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 10, 20, 23, 25, 24, 247725)),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 10, 20, 23, 25, 24, 246728)),
        ),
        migrations.AlterField(
            model_name='purchases',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 10, 20, 23, 25, 24, 247725)),
        ),
    ]