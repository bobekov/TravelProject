# Generated by Django 5.1.3 on 2024-11-17 13:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0001_initial'),
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingflight',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight.flight'),
        ),
    ]