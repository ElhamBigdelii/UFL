# Generated by Django 2.1.5 on 2020-02-06 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0020_auto_20200204_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charity',
            name='modir',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]