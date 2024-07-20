# Generated by Django 4.2.13 on 2024-07-14 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctorapp', '0004_registeration_last_login'),
        ('userapp', '0002_remove_bookingitem_quantity_booking_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='approval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bkngdate', models.DateField()),
                ('cnsultdate', models.DateTimeField()),
                ('books', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userapp.booking')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='doctorapp.registeration')),
            ],
        ),
    ]