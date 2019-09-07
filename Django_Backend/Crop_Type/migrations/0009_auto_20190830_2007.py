# Generated by Django 2.1.7 on 2019-08-30 20:07

import Crop_Type.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crop_Type', '0008_auto_20181031_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop',
            name='crop_type',
        ),
        migrations.AddField(
            model_name='crop',
            name='farmImage',
            field=models.ImageField(default='farm.jpg', upload_to=Crop_Type.models.image_upload_path),
        ),
    ]
