# Generated by Django 4.1.7 on 2023-04-14 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_callanalitics_data_delete_callanalytics_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]