# Generated by Django 3.2 on 2021-11-01 19:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit',
            name='Date',
            field=models.DateField(default=datetime.date(2021, 11, 2), verbose_name=datetime.date(2021, 11, 2)),
        ),
        migrations.AddField(
            model_name='debit',
            name='Date',
            field=models.DateField(default=datetime.date(2021, 11, 2), verbose_name=datetime.date(2021, 11, 2)),
        ),
    ]