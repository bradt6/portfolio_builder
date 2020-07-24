# Generated by Django 3.0.6 on 2020-07-24 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0002_auto_20200724_0314'),
        ('portfolio', '0006_auto_20200518_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='builder',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='builder.Builder'),
        ),
    ]
