# Generated by Django 3.2.6 on 2021-08-23 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables_reservations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('table_number', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='table',
            name='reserved_status',
        ),
    ]
