# Generated by Django 5.0.6 on 2025-03-29 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='section',
            name='type_game',
            field=models.IntegerField(choices=[(0, 'No game'), (1, 'Game 1'), (2, 'Game 2'), (3, 'Game 3')]),
        ),
    ]
