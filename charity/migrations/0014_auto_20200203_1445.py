# Generated by Django 2.1.5 on 2020-02-03 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0013_project_cration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttype',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
