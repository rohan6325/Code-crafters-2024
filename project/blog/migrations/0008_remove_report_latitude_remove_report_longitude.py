# Generated by Django 4.1.5 on 2024-04-02 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_report_latitude_report_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='report',
            name='longitude',
        ),
    ]