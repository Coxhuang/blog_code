# Generated by Django 2.0.7 on 2019-11-27 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0003_auto_20191127_0040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='tags',
            new_name='tag',
        ),
    ]
