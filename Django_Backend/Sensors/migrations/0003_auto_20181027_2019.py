# Generated by Django 2.1.2 on 2018-10-27 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Sensors', '0002_auto_20181027_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensordata',
            name='parent_sensor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_sensor', to='Sensors.Sensor'),
        ),
    ]
