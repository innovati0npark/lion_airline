# Generated by Django 5.0.6 on 2024-05-24 09:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_ticket'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure', models.CharField(max_length=100)),
                ('departure_airport', models.CharField(max_length=100)),
                ('departure_airport_code', models.CharField(max_length=10)),
                ('destination', models.CharField(max_length=100)),
                ('destination_airport', models.CharField(max_length=100)),
                ('destination_airport_code', models.CharField(max_length=10)),
                ('departure_date', models.DateField()),
                ('destination_date', models.DateField()),
                ('departure_time', models.TimeField()),
                ('destination_time', models.TimeField()),
                ('duration', models.CharField(max_length=100)),
                ('airline', models.CharField(max_length=100)),
                ('flightClass', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='ticket',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
