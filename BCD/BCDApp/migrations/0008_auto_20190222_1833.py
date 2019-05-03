# Generated by Django 2.0.3 on 2019-02-22 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BCDApp', '0007_auto_20190214_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='CIOHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CIO_ID', models.CharField(max_length=30)),
                ('CIO_Name', models.CharField(max_length=30)),
                ('CIO_Email', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='bcd',
            name='COE_Comments',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bcd',
            name='Finance_Comments',
            field=models.CharField(max_length=50, null=True),
        ),
    ]