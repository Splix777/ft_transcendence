# Generated by Django 3.2.23 on 2024-01-30 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_tournament_public'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='joinable',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='public',
        ),
    ]
