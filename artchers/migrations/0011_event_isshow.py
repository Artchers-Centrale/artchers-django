# Generated by Django 5.0.3 on 2024-03-30 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artchers', '0010_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='isShow',
            field=models.BooleanField(default=False),
        ),
    ]
