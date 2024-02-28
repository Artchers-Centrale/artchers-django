# Generated by Django 5.0.2 on 2024-02-24 17:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='district',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='')),
                ('image_el', models.FileField(upload_to='')),
                ('is_eliminated', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=200)),
                ('nom', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=200)),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artchers.district')),
            ],
        ),
    ]