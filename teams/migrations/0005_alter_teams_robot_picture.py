# Generated by Django 4.2.9 on 2024-02-10 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_alter_team_match_data_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='robot_picture',
            field=models.URLField(blank=True, null=True),
        ),
    ]