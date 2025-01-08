# Generated by Django 5.0.4 on 2025-01-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("freedomrun", "0014_alter_individual_category_alter_team_family_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="individual",
            name="category",
            field=models.CharField(
                choices=[
                    ("", "Choose category "),
                    ("5 Km Walk", "5 Kms Walk"),
                    ("5 Km Run", "5 Kms Run"),
                    ("10 Km Run", "10 Kms Run"),
                ],
                default="5 Km Walk",
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="team_family",
            name="category",
            field=models.CharField(
                choices=[
                    ("", "Choose category "),
                    ("5 Km Walk", "5 Kms Walk"),
                    ("5 Km Run", "5 Kms Run"),
                    ("10 Km Run", "10 Kms Run"),
                ],
                default="5 Km Walk",
                max_length=20,
                null=True,
            ),
        ),
    ]