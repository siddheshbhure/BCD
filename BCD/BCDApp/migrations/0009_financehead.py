# Generated by Django 2.0.3 on 2019-02-22 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BCDApp', '0008_auto_20190222_1833'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinanceHead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fin_ID', models.CharField(max_length=30)),
                ('Fin_Name', models.CharField(max_length=30)),
                ('Fin_Email', models.CharField(max_length=50)),
            ],
        ),
    ]