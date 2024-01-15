# Generated by Django 5.0.1 on 2024-01-08 18:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_alter_auction_duration_alter_auction_has_ended'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='current_price',
            field=models.IntegerField(default=1, editable=False),
        ),
        migrations.AlterField(
            model_name='auction',
            name='duration',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 15, 19, 15, 23, 708264)),
        ),
    ]