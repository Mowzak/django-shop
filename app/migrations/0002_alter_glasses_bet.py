# Generated by Django 3.2 on 2021-08-04 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glasses',
            name='bet',
            field=models.TextField(default='', max_length=25, verbose_name='پیش نویس'),
        ),
    ]
