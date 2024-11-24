# Generated by Django 5.1.3 on 2024-11-17 13:44

import django.core.validators
import django.db.models.deletion
import travel_project.user_profile.managers
import travel_project.user_profile.validators
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', travel_project.user_profile.managers.AppUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('username', models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(3), travel_project.user_profile.validators.validate_profile_name])),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, validators=[travel_project.user_profile.validators.validate_phone_number])),
                ('address', models.CharField(blank=True, max_length=40, null=True)),
                ('info', models.TextField(blank=True, null=True)),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
