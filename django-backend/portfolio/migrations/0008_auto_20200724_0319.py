# Generated by Django 3.0.6 on 2020-07-24 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0002_auto_20200724_0314'),
        ('portfolio', '0007_portfolio_builder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='builder',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='builder.Builder'),
        ),
    ]