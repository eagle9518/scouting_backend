# Generated by Django 4.1.6 on 2023-02-17 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Matches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantifier', models.CharField(max_length=10)),
                ('match_number', models.IntegerField()),
                ('red_one', models.IntegerField()),
                ('red_two', models.IntegerField()),
                ('red_three', models.IntegerField()),
                ('blue_one', models.IntegerField()),
                ('blue_two', models.IntegerField()),
                ('blue_three', models.IntegerField()),
            ],
        ),
    ]
