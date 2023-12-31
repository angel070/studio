# Generated by Django 4.2.3 on 2023-11-19 14:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studio_app', '0004_remove_returnedcomponents_status_alter_expenses_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchases',
            name='file',
            field=models.FileField(null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 11, 19, 17, 21, 54, 362919)),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 11, 19, 17, 21, 54, 356887)),
        ),
        migrations.AlterField(
            model_name='purchases',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 11, 19, 17, 21, 54, 358937)),
        ),
    ]
