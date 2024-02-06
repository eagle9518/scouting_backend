# Generated by Django 4.2.9 on 2024-02-06 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_teams_width'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_match_data',
            name='comment',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='teams',
            name='additional_info',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
