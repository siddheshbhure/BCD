# Generated by Django 2.1.5 on 2019-03-13 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BCDApp', '0023_auto_20190313_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prgrid',
            name='Bid_1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='prgrid',
            name='Bid_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='prgrid',
            name='Bid_3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='prgrid',
            name='Budget_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='prgrid',
            name='Quantity',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='prgrid',
            name='Tech_spoc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='prgrid',
            name='Vendor_1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='prgrid',
            name='Vendor_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='prgrid',
            name='Vendor_3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='prgrid',
            name='end_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='prgrid',
            name='new_unit_rate',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='prgrid',
            name='old_unit_rate',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='prgrid',
            name='procurement_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='prgrid',
            name='start_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='prgrid',
            name='type_of_expense',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='prgrid',
            name='vendor_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
