# Generated by Django 2.1.5 on 2019-03-12 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BCDApp', '0021_auto_20190312_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prgrid',
            name='start_date',
            field=models.CharField(max_length=50),
        ),
    ]
