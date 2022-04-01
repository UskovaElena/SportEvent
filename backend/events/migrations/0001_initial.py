# Generated by Django 3.2.5 on 2022-03-29 18:36

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.CharField(choices=[(1, 'football'), (2, 'bike'), (3, 'running'), (4, 'pilates')], default='running', max_length=100)),
                ('date', models.DateField(validators=[django.core.validators.MinValueValidator(datetime.date(2022, 3, 29)), django.core.validators.MaxValueValidator(datetime.date(2022, 4, 29))])),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('person_number', models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(15)])),
                ('level', models.CharField(choices=[(1, 'None'), (2, 'Low'), (3, 'Medium'), (4, 'Hard')], default='None', max_length=100)),
                ('latitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)])),
                ('longitude', models.FloatField(validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
