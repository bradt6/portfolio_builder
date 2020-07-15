# Generated by Django 3.0.6 on 2020-07-07 02:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageManager',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('about', models.BooleanField()),
                ('portfolio', models.BooleanField()),
                ('services', models.BooleanField()),
                ('home', models.BooleanField()),
                ('contact', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('cdn_url_path', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Builder',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('pageManager', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='builder.PageManager')),
                ('template', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='builder.Template')),
            ],
        ),
    ]