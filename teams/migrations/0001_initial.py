# Generated by Django 4.1.6 on 2024-01-19 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_number', models.IntegerField(unique=True)),
                ('robot_picture', models.ImageField(upload_to='')),
                ('drivetrain', models.CharField(max_length=32)),
                ('primary_role', models.CharField(max_length=32)),
                ('additional_info', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Team_Match_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_number', models.IntegerField()),
                ('quantifier', models.CharField(max_length=10)),
                ('auto_leave', models.IntegerField()),
                ('auto_amp', models.IntegerField()),
                ('auto_speaker_make', models.IntegerField()),
                ('auto_speaker_miss', models.IntegerField()),
                ('teleop_amp', models.IntegerField()),
                ('teleop_speaker_make', models.IntegerField()),
                ('teleop_speaker_miss', models.IntegerField()),
                ('trap', models.IntegerField()),
                ('climb', models.IntegerField()),
                ('driver_ranking', models.IntegerField()),
                ('defense_ranking', models.IntegerField()),
                ('comment', models.CharField(max_length=128)),
                ('scout_name', models.CharField(max_length=32)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_match_data', to='teams.teams')),
            ],
        ),
    ]
