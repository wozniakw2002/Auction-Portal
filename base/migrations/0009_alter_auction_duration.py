# Generated by Django 5.0.1 on 2024-01-08 17:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_auction_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='duration',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 15, 18, 52, 35, 94887)),
        ),
    ]
