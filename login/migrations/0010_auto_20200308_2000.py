# Generated by Django 3.0.3 on 2020-03-08 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20200308_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userba',
            old_name='tel',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='usercenter',
            old_name='tel',
            new_name='phone',
        ),
    ]
