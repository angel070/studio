# Generated by Django 4.2.3 on 2023-11-12 17:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studio_app', '0002_remove_respondedcomponents_component_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 11, 12, 20, 25, 4, 282003)),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 11, 12, 20, 25, 4, 281007)),
        ),
        migrations.AlterField(
            model_name='purchases',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 11, 12, 20, 25, 4, 282003)),
        ),
        migrations.CreateModel(
            name='ReturnedComponents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(max_length=255, null=True)),
                ('responseDate', models.DateTimeField(blank=True, null=True)),
                ('respondedComponent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='studio_app.respondedcomponents')),
            ],
            options={
                'verbose_name_plural': 'Returned Components',
            },
        ),
    ]
