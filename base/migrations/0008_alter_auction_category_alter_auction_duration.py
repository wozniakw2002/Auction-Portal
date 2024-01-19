# Generated by Django 5.0.1 on 2024-01-18 17:39

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_auction_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='category',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.category'),
        ),
        migrations.AlterField(
            model_name='auction',
            name='duration',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 25, 18, 39, 26, 395951)),
        ),
    ]