# Generated by Django 5.0.3 on 2024-03-25 05:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tshirt_Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=250)),
                ('gender', models.CharField(max_length=250)),
                ('phone_no', models.CharField(max_length=10)),
                ('area', models.TextField()),
                ('registration_fee', models.DecimalField(decimal_places=2, default=500.0, max_digits=10)),
                ('tshirt_size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='freedomrun.tshirt_size')),
            ],
        ),
    ]
