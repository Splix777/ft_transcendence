# Generated by Django 3.2.23 on 2024-01-31 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0003_auto_20240130_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='joinable',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tournament',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]