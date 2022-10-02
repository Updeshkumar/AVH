# Generated by Django 4.0.3 on 2022-09-30 15:58

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
                ('vehiname', models.CharField(max_length=100)),
                ('experinyear', models.CharField(max_length=200)),
                ('drivername', models.CharField(max_length=150)),
                ('aadharnumber', models.CharField(max_length=20)),
                ('mobilenumber', models.CharField(max_length=12)),
                ('alternetmobilenumber', models.CharField(max_length=12)),
                ('licensenumber', models.CharField(max_length=200)),
                ('uploadlicense', models.ImageField(blank=True, upload_to='pimages')),
                ('uploaddriverphoto', models.ImageField(blank=True, upload_to='pimages')),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('tehsil', models.CharField(max_length=50)),
            ],
        ),
    ]