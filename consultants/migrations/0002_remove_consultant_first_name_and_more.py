# Generated by Django 4.2 on 2024-10-11 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consultants', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultant',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='consultant',
            name='last_name',
        ),
    ]
