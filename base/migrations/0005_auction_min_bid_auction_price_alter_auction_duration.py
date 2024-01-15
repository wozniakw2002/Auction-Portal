# Generated by Django 5.0.1 on 2024-01-08 17:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_item_pictrue_alter_auction_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='min_bid',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='auction',
            name='price',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='auction',
            name='duration',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 15, 18, 47, 40, 541630)),
        ),
    ]
