# Generated by Django 3.0.6 on 2020-05-18 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_auto_20200518_0353'),
        ('portfolio', '0005_auto_20200518_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='images',
            field=models.ManyToManyField(blank=True, to='images.Image'),
        ),
    ]
