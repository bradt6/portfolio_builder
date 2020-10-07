# Generated by Django 3.0.6 on 2020-10-07 04:37

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], unique=True)),
                ('from_hour', models.TimeField()),
                ('to_hour', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.IntegerField(choices=[(1, 'Facebook'), (2, 'Instagram'), (3, 'Twitter'), (4, 'Youtube'), (5, 'Linkedin')])),
                ('account_url', models.URLField()),
                ('social_icon', models.CharField(editable=False, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_bussiness', models.CharField(max_length=27)),
                ('description', models.TextField()),
                ('business_number', models.CharField(max_length=27)),
                ('license_number', models.CharField(blank=True, max_length=27)),
                ('lat', models.DecimalField(decimal_places=8, max_digits=10)),
                ('lng', models.DecimalField(decimal_places=8, max_digits=11)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='images.Image')),
                ('opening_times', models.ManyToManyField(blank=True, to='about.OpeningHours')),
                ('social_accounts', models.ManyToManyField(blank=True, to='about.SocialMediaAccount')),
            ],
        ),
    ]
