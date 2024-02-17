# Generated by Django 4.2.9 on 2024-02-16 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HumanPlayerMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_number', models.IntegerField()),
                ('event', models.CharField(default='testing', max_length=16)),
                ('match_number', models.IntegerField()),
                ('human_player_timing', models.IntegerField(default=0)),
                ('human_player_spotlit', models.IntegerField(default=0)),
                ('strategist_name', models.CharField(default='', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Team_Match_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_number', models.IntegerField()),
                ('event', models.CharField(default='testing', max_length=16)),
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
                ('comment', models.CharField(max_length=256)),
                ('scout_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_number', models.IntegerField()),
                ('event', models.CharField(default='testing', max_length=16)),
                ('robot_picture', models.URLField(blank=True, null=True)),
                ('drivetrain', models.CharField(max_length=32)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('width', models.IntegerField(blank=True, null=True)),
                ('additional_info', models.CharField(blank=True, max_length=256, null=True)),
                ('pit_scout_status', models.BooleanField(default=False)),
            ],
        ),
    ]
