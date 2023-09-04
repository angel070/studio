# Generated by Django 4.2.3 on 2023-08-27 14:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studio_app', '0004_alter_expenses_date_alter_income_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 27, 17, 42, 27, 20683)),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 27, 17, 42, 27, 19686)),
        ),
        migrations.AlterField(
            model_name='purchases',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 8, 27, 17, 42, 27, 20683)),
        ),
        migrations.CreateModel(
            name='RespondedComponents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(max_length=255, null=True)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='studio_app.component')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studio_app.request')),
            ],
            options={
                'verbose_name_plural': 'Request Components',
            },
        ),
    ]
