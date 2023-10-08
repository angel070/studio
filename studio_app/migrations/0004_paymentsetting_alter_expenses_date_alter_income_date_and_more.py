# Generated by Django 4.2.3 on 2023-10-08 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio_app', '0003_remove_member_deparment_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 10, 8, 17, 23, 26, 167638)),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 10, 8, 17, 23, 26, 167638)),
        ),
        migrations.AlterField(
            model_name='purchases',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 10, 8, 17, 23, 26, 167638)),
        ),
    ]
