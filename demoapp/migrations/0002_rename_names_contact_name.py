# Generated by Django 5.2 on 2025-04-13 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='names',
            new_name='name',
        ),
    ]
