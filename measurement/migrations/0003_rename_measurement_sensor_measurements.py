# Generated by Django 4.2.4 on 2023-08-04 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_sensor_measurement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='measurement',
            new_name='measurements',
        ),
    ]
