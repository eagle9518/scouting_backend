# Generated by Django 4.2.9 on 2024-01-23 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='additional_info',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='length',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='robot_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='teams',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
