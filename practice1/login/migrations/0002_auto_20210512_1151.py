# Generated by Django 3.1.4 on 2021-05-12 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labour',
            old_name='name',
            new_name='lname',
        ),
    ]