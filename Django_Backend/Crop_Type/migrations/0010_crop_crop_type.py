# Generated by Django 2.1.7 on 2019-08-30 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crop_Type', '0009_auto_20190830_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='crop_type',
            field=models.CharField(choices=[('Kharif crops', 'Kharif crops'), ('Rabi Crops', 'Rabi Crops'), ('Zaid Crop', 'Zaid Crop'), ('Rice', 'Rice'), ('Wheat', 'Wheat'), ('Pulses', 'Pulses'), ('Sugarcane', 'Sugarcane'), ('Cotton', 'Cotton'), ('Groundnut', 'Groundnut'), ('Tea', 'Tea'), ('Coffee', 'Coffee')], default='Pulses', max_length=20),
        ),
    ]
