# Generated by Django 2.0.3 on 2019-02-25 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BCDApp', '0009_financehead'),
    ]

    operations = [
        migrations.AddField(
            model_name='bcd',
            name='CIO_Comments',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bcd',
            name='CIO_status',
            field=models.CharField(default='Pending', max_length=30),
            preserve_default=False,
        ),
    ]
