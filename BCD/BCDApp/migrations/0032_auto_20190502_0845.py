# Generated by Django 2.1.5 on 2019-05-02 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BCDApp', '0031_auto_20190502_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prgrid',
            name='new_unit_rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='prgrid',
            name='old_unit_rate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]
