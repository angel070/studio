# Generated by Django 4.2.3 on 2023-08-16 07:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio_app', '0006_alter_expenses_date_alter_income_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='email',
        ),
        migrations.AlterField(
            model_name='component',
            name='cost',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='component',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 16, 10, 36, 54, 13017)),
        ),
        migrations.AlterField(
            model_name='income',
            name='amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 16, 10, 36, 54, 13017)),
        ),
        migrations.AlterField(
            model_name='purchases',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 16, 10, 36, 54, 13017)),
        ),
        migrations.AlterField(
            model_name='requestcomponents',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
