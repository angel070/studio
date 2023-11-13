# Generated by Django 4.2.3 on 2023-11-13 03:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio_app', '0003_alter_expenses_date_alter_income_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='returnedcomponents',
            name='status',
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 11, 13, 6, 46, 41, 184427)),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 11, 13, 6, 46, 41, 184427)),
        ),
        migrations.AlterField(
            model_name='purchases',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 11, 13, 6, 46, 41, 184427)),
        ),
    ]