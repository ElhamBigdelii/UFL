# Generated by Django 2.1.5 on 2020-02-03 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0011_auto_20200203_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='endDate',
        ),
        migrations.RemoveField(
            model_name='project',
            name='publishDate',
        ),
        migrations.RemoveField(
            model_name='project',
            name='rejistrationDate',
        ),
        migrations.RemoveField(
            model_name='project',
            name='startDate',
        ),
    ]
