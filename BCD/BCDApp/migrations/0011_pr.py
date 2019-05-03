# Generated by Django 2.0.3 on 2019-02-27 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BCDApp', '0010_auto_20190225_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='PR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PR_No', models.CharField(max_length=30)),
                ('Request_date', models.DateField()),
                ('Application_system', models.CharField(max_length=30)),
                ('Budget', models.CharField(max_length=30)),
                ('Business', models.CharField(max_length=30)),
                ('Start_date', models.DateField()),
                ('End_date', models.DateField()),
                ('Number_of_months', models.CharField(max_length=30)),
                ('BCD_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='BCDs', to='BCDApp.BCD')),
            ],
        ),
    ]
