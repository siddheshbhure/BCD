# Generated by Django 2.1.5 on 2019-02-11 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BCD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BCD_no', models.CharField(max_length=30)),
                ('requestor_ID', models.CharField(default='00000', max_length=20)),
                ('requestor_name', models.CharField(max_length=30)),
                ('BCD_amount', models.CharField(max_length=30)),
                ('BCD_overview', models.CharField(max_length=100)),
                ('status', models.CharField(default='Pending with COE', max_length=40)),
                ('pdf', models.FileField(blank=True, upload_to='docs/', verbose_name='Upload BCD')),
            ],
        ),
        migrations.CreateModel(
            name='COEHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('COE_ID', models.CharField(max_length=30)),
                ('COE_Name', models.CharField(max_length=30)),
                ('COE_Email', models.CharField(max_length=30)),
            ],
        ),
    ]