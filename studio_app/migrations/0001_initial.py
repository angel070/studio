# Generated by Django 4.2.3 on 2023-08-23 11:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=20)),
                ('quantity', models.PositiveIntegerField()),
                ('cost', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Components',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Labs',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Location',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('middleName', models.CharField(blank=True, max_length=255, null=True)),
                ('lastName', models.CharField(max_length=255)),
                ('dateOfBirth', models.DateField()),
                ('registrationNumber', models.CharField(max_length=255)),
                ('phoneNumber', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('idNumber', models.CharField(max_length=255)),
                ('registeredDate', models.DateField(null=True)),
                ('nationality', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=255)),
                ('deparment', models.CharField(max_length=255)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='studio_app.department')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='studio_app.location')),
            ],
            options={
                'verbose_name_plural': 'Members',
            },
        ),
        migrations.CreateModel(
            name='Member_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Member Type',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestedDate', models.DateTimeField(auto_now_add=True)),
                ('requested', models.BooleanField(null=True)),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='studio_app.member')),
            ],
            options={
                'verbose_name_plural': 'Requests',
            },
        ),
        migrations.CreateModel(
            name='Source_Of_Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Source Of Expenses',
            },
        ),
        migrations.CreateModel(
            name='Source_of_Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Source-of-Income',
            },
        ),
        migrations.CreateModel(
            name='Requestcomponents',
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
        migrations.CreateModel(
            name='Purchases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('amount', models.FloatField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('date', models.DateField(default=datetime.datetime(2023, 8, 23, 14, 6, 43, 586263))),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='studio_app.component')),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='studio_app.lab')),
            ],
            options={
                'verbose_name_plural': 'Purchases',
            },
        ),
        migrations.AddField(
            model_name='member',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='studio_app.member_type'),
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('date', models.DateField(default=datetime.datetime(2023, 8, 23, 14, 6, 43, 586263))),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='studio_app.lab')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='studio_app.source_of_income')),
            ],
            options={
                'verbose_name_plural': 'Income',
            },
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('date', models.DateField(default=datetime.datetime(2023, 8, 23, 14, 6, 43, 586263))),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='studio_app.lab')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='studio_app.source_of_expenses')),
            ],
            options={
                'verbose_name_plural': 'Expenses',
            },
        ),
        migrations.AddField(
            model_name='component',
            name='lab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='studio_app.lab'),
        ),
        migrations.CreateModel(
            name='CheckInAndout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('status', models.CharField(max_length=255)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='studio_app.member')),
            ],
            options={
                'verbose_name_plural': 'CheckInAndout',
            },
        ),
    ]
