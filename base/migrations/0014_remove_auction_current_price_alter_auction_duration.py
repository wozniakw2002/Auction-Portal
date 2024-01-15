# Generated by Django 5.0.1 on 2024-01-08 18:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_auction_current_price_alter_auction_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='current_price',
        ),
        migrations.AlterField(
            model_name='auction',
            name='duration',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 15, 19, 9, 27, 684074)),
        ),
    ]