# Generated by Django 3.0.6 on 2020-09-24 02:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20200521_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='description_of_job',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]