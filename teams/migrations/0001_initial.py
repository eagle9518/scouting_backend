# Generated by Django 4.1.6 on 2023-02-13 07:55

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
            ],
        ),
        migrations.CreateModel(
            name='Team_Match_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_number', models.IntegerField()),
                ('auto_charging_station', models.IntegerField()),
                ('auto_cones', models.IntegerField()),
                ('auto_cubes', models.IntegerField()),
                ('teleop_cones', models.IntegerField()),
                ('teleop_cubes', models.IntegerField()),
                ('cone_transport', models.IntegerField()),
                ('cube_transport', models.IntegerField()),
                ('end_charging_station', models.IntegerField()),
                ('total_points', models.IntegerField()),
                ('driver_ranking', models.IntegerField()),
                ('defense_ranking', models.IntegerField()),
                ('comment', models.CharField(max_length=128)),
                ('scout_name', models.CharField(max_length=32)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_data', to='teams.teams')),
            ],
        ),
    ]
