# Generated by Django 2.2 on 2020-05-03 13:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0006_auto_20200503_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]