# Generated by Django 4.2.13 on 2024-07-19 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorapp', '0008_userdiaganosis_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='docname',
            field=models.CharField(max_length=200, null=True),
        ),
    ]