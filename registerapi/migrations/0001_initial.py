# Generated by Django 4.0.3 on 2022-10-02 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('phonenumber', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=150)),
                ('tehsil', models.CharField(max_length=230)),
            ],
        ),
    ]
