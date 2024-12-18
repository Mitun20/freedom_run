# Generated by Django 5.0.4 on 2024-07-22 05:56

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freedomrun', '0011_location_alter_individual_location_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.RemoveField(
            model_name='individual',
            name='location',
        ),
        migrations.RemoveField(
            model_name='member',
            name='location',
        ),
        migrations.AddField(
            model_name='individual',
            name='category',
            field=models.CharField(choices=[('', 'Choose category '), ('5 Km', '5 Kms'), ('10 Km', '10 Kms')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='individual',
            name='chest_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='chest_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='team_family',
            name='category',
            field=models.CharField(choices=[('', 'Choose category '), ('5 Km', '5 Kms'), ('10 Km', '10 Kms')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='coupen',
            name='percentage',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=5),
        ),
        migrations.AlterField(
            model_name='individual',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='team_family',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
