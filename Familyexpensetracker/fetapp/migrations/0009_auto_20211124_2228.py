# Generated by Django 3.2.3 on 2021-11-24 16:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fetapp', '0008_auto_20211124_2226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_new_member',
            old_name='Mobileno',
            new_name='Mobile_no',
        ),
        migrations.AlterField(
            model_name='add_new_expenses',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 24, 22, 28, 30, 848506), verbose_name='date published'),
        ),
    ]
