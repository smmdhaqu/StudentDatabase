# Generated by Django 2.2 on 2020-05-01 03:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('user_name', models.CharField(blank=True, max_length=30, null=True)),
                ('user_email', models.CharField(blank=True, max_length=30, null=True)),
                ('user_phone', models.CharField(blank=True, max_length=30, null=True)),
                ('user_picture', models.ImageField(blank=True, default='profile.png', upload_to='profile_pic')),
                ('user_bloodGroup', models.CharField(blank=True, max_length=30, null=True)),
                ('user_gender', models.CharField(blank=True, max_length=30, null=True)),
                ('user_address', models.CharField(blank=True, max_length=100, null=True)),
                ('user_city', models.CharField(blank=True, max_length=30, null=True)),
                ('user_state', models.CharField(blank=True, max_length=30, null=True)),
                ('user_zip', models.IntegerField(blank=True, null=True)),
                ('user_school', models.CharField(blank=True, max_length=100, null=True)),
                ('user_college', models.CharField(blank=True, max_length=100, null=True)),
                ('user_university', models.CharField(blank=True, max_length=100, null=True)),
                ('user_department', models.CharField(blank=True, max_length=30, null=True)),
                ('user_fbId', models.CharField(blank=True, max_length=30, null=True)),
                ('user_bio', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
