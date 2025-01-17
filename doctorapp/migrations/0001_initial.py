# Generated by Django 4.2.13 on 2024-07-10 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='registeration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('phonenum', models.IntegerField()),
                ('adrs', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('mail', models.EmailField(max_length=254)),
                ('pwd', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('usertype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('staffposition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorapp.position')),
            ],
        ),
    ]
