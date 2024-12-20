# Generated by Django 5.0.4 on 2024-04-30 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freedomrun', '0008_individual_is_paid_individual_paid_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='team_family',
            name='is_paid',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='team_family',
            name='paid_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
