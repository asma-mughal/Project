# Generated by Django 4.0.3 on 2022-07-07 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_competitions_cmp_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('User_Name', models.CharField(max_length=120)),
                ('User_LastName', models.CharField(max_length=120)),
                ('User_email', models.EmailField(max_length=120)),
                ('User_agreement', models.BooleanField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Name', models.CharField(max_length=120)),
                ('User_LastName', models.CharField(blank=True, max_length=120, null=True)),
                ('User_email', models.EmailField(max_length=120)),
                ('User_phone', models.CharField(max_length=120)),
                ('User_enquiry', models.CharField(max_length=150)),
                ('User_Consent', models.BooleanField()),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
