# Generated by Django 5.1.3 on 2024-11-17 13:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(choices=[('SINGLE', 'SINGLE'), ('DOUBLE', 'DOUBLE'), ('SUITE', 'SUITE'), ('FAMILY', 'FAMILY'), ('DELUXE', 'DELUXE'), ('STUDIO', 'STUDIO')], max_length=40)),
                ('room_number', models.CharField(max_length=500)),
                ('price_per_night', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('description', models.TextField(blank=True, null=True)),
                ('air_conditioning', models.BooleanField(default=False)),
                ('bathtub', models.BooleanField(default=False)),
                ('tv', models.BooleanField(default=False)),
                ('balcony', models.BooleanField(default=False)),
                ('available', models.BooleanField(default=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel')),
            ],
        ),
    ]