# Generated by Django 5.0.1 on 2024-01-18 17:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_auction_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='duration',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 25, 18, 40, 2, 918154)),
        ),
    ]