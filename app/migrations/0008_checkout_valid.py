# Generated by Django 3.0.4 on 2021-09-06 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210830_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='valid',
            field=models.BooleanField(default=False),
        ),
    ]