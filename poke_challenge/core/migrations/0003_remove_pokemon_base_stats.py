# Generated by Django 3.2.5 on 2021-07-05 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_stat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='base_stats',
        ),
    ]