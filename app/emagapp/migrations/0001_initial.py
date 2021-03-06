# Generated by Django 3.1.2 on 2020-10-27 13:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('dept_name', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_no', models.CharField(blank=True, max_length=10, null=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Administrator',
                'verbose_name_plural': 'Administrators',
                'db_table': 'Administrators',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
            ],
            options={
                'verbose_name': 'Subscriber',
                'verbose_name_plural': 'Subscribers',
                'db_table': 'Subscribers',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=755, unique=True)),
                ('project_description', models.TextField()),
                ('project_tags', models.CharField(blank=True, max_length=400, null=True)),
                ('project_data', models.FileField(blank=True, null=True, upload_to='')),
                ('project_banner', models.ImageField(blank=True, null=True, upload_to='')),
                ('uploaded_at', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'db_table': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=755, unique=True)),
                ('event_category', models.CharField(choices=[('Fest', 'Fest'), ('Workshop', 'Workshop'), ('Activity', 'Activity')], max_length=400)),
                ('event_tags', models.CharField(blank=True, max_length=400, null=True)),
                ('organised_by', models.CharField(blank=True, max_length=1000, null=True)),
                ('sponsored_by', models.CharField(blank=True, max_length=1000, null=True)),
                ('event_data', models.FileField(blank=True, null=True, upload_to='')),
                ('event_banner', models.ImageField(blank=True, null=True, upload_to='')),
                ('event_description', models.TextField()),
                ('event_date', models.DateField()),
                ('uploaded_at', models.DateField(default=datetime.date.today)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'db_table': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievement_title', models.CharField(max_length=755, unique=True)),
                ('achievement_field', models.CharField(max_length=400)),
                ('achievement_data', models.FileField(blank=True, null=True, upload_to='')),
                ('achievement_banner', models.ImageField(blank=True, null=True, upload_to='')),
                ('achievement_tags', models.CharField(blank=True, max_length=400, null=True)),
                ('achievement_description', models.TextField()),
                ('uploaded_at', models.DateField(default=datetime.date.today)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='achievements', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Achievement',
                'verbose_name_plural': 'Achievements',
                'db_table': 'Achievements',
            },
        ),
    ]
