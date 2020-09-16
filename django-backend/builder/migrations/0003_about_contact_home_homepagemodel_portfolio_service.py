# Generated by Django 3.0.6 on 2020-09-15 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0002_auto_20200724_0314'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(default=False)),
                ('icon', models.ImageField(default=None, upload_to='')),
                ('name', models.CharField(default='about', editable=False, max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(default=False)),
                ('icon', models.ImageField(default=None, upload_to='')),
                ('name', models.CharField(default='contact', editable=False, max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(default=False)),
                ('icon', models.ImageField(default=None, upload_to='')),
                ('name', models.CharField(default='home', editable=False, max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomePageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(upload_to='')),
                ('call_to_action_text', models.CharField(max_length=27)),
                ('short_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(default=False)),
                ('icon', models.ImageField(default=None, upload_to='')),
                ('name', models.CharField(default='portfolio', editable=False, max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isActive', models.BooleanField(default=False)),
                ('icon', models.ImageField(default=None, upload_to='')),
                ('name', models.CharField(choices=[('services', 'Services'), ('skills', 'Skills')], default='service', max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]