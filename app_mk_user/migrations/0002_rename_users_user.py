# Generated by Django 4.2.6 on 2023-10-13 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_mk_user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='users',
            new_name='user',
        ),
    ]
