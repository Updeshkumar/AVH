# Generated by Django 4.0.3 on 2022-09-30 06:40

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
                ('vehivalname', models.CharField(max_length=50)),
                ('modelnumber', models.CharField(max_length=100)),
                ('ownername', models.CharField(max_length=20)),
                ('aadharnumber', models.CharField(max_length=20)),
                ('mobilenumber', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=50)),
                ('state', models.CharField(max_length=10)),
                ('district', models.CharField(max_length=10)),
                ('tehsil', models.CharField(max_length=10)),
                ('uvp', models.ImageField(blank=True, upload_to='pimages')),
            ],
        ),
    ]
