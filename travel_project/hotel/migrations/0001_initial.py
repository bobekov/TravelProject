# Generated by Django 5.1.3 on 2024-11-17 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('star_rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('photo', models.URLField()),
                ('facilities', models.TextField(help_text='e.g. parking, free Wi-Fi, pool, gym, spa, airport transfer, room service')),
                ('check_in_time', models.TimeField()),
                ('available_rooms', models.PositiveIntegerField(default=0)),
                ('address', models.CharField(max_length=100)),
                ('payment_method', models.CharField(choices=[('CREDIT_CARD', 'Credit Card'), ('PAYPAL', 'Paypal'), ('BANK_TRANSFER', 'Bank Transfer')], max_length=30)),
            ],
        ),
    ]