# Generated by Django 3.2.6 on 2021-08-25 16:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('follow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='follow',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
