# Generated by Django 2.1.7 on 2019-09-26 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crop_Type', '0014_crop_cropimageannotated'),
    ]

    operations = [
        migrations.AddField(
            model_name='crop',
            name='altitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='crop',
            name='total_crops',
            field=models.FloatField(default=0.0),
        ),
    ]
