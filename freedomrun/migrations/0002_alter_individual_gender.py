# Generated by Django 5.0.3 on 2024-03-25 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freedomrun', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual',
            name='gender',
            field=models.CharField(choices=[('', 'Choose Gender'), ('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1),
        ),
    ]
