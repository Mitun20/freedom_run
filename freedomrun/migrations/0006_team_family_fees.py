# Generated by Django 5.0.4 on 2024-04-27 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freedomrun', '0005_individual_registered_date_member_registered_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team_family',
            name='fees',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
