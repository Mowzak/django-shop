# Generated by Django 3.2 on 2021-08-04 05:42

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='glasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='موضوع')),
                ('bet', models.CharField(default='', max_length=25, verbose_name='پیش نویس')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='متن')),
                ('price', models.CharField(default='0', max_length=20, verbose_name='قیمت')),
                ('image', models.ImageField(blank=True, default='def.jpg', upload_to='img/', verbose_name='عکس')),
                ('image2', models.ImageField(blank=True, default='def.jpg', upload_to='img/', verbose_name='عکس')),
                ('image3', models.ImageField(blank=True, default='def.jpg', upload_to='img/', verbose_name='عکس')),
            ],
            options={
                'verbose_name': 'عینک',
                'verbose_name_plural': 'عینک ها',
            },
        ),
        migrations.CreateModel(
            name='homeview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=50, verbose_name='متن')),
                ('textb', models.CharField(default='shop now', max_length=50, verbose_name='متن دکمه')),
                ('image', models.ImageField(blank=True, default='def.jpg', upload_to='img/', verbose_name='عکس')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'متن ها در صفحه ی اصلی',
            },
        ),
        migrations.CreateModel(
            name='us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='متن')),
                ('text1', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='متن')),
                ('text2', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='متن')),
                ('text3', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='متن')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'درباره ی ما',
            },
        ),
        migrations.CreateModel(
            name='savee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_save', models.ManyToManyField(default=None, to='app.glasses')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ذخیره',
                'verbose_name_plural': 'ذخیره شده ها',
            },
        ),
        migrations.CreateModel(
            name='like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likee', models.ManyToManyField(default=None, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.glasses')),
            ],
            options={
                'verbose_name': 'لایک',
                'verbose_name_plural': 'لایک ها',
            },
        ),
        migrations.CreateModel(
            name='fav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav', models.ManyToManyField(default=None, to='app.glasses')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'پست های منتخب',
            },
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(default='', max_length=150, verbose_name='نظرات')),
                ('active', models.BooleanField(default=True, verbose_name='وضعیت')),
                ('proid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.glasses', verbose_name='محصول')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرات',
                'ordering': ['active'],
            },
        ),
    ]