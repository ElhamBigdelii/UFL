# Generated by Django 2.1.5 on 2020-02-03 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0015_project_kheiriye'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='projectType',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='charity.ProjectType'),
        ),
    ]