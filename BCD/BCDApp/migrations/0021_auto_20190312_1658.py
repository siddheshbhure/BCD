# Generated by Django 2.1.5 on 2019-03-12 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BCDApp', '0020_auto_20190312_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prgrid',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]