# Generated by Django 4.0.3 on 2022-09-30 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Doregistration', '0002_alter_profile_vehiname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='vehiname',
            new_name='vehicalname',
        ),
    ]
