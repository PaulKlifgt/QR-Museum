# Generated by Django 5.0.6 on 2025-03-29 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_section_type_game_exhibit_type_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibit',
            name='average_rank',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='exhibit',
            name='count_rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='section',
            name='average_rank',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='section',
            name='count_rank',
            field=models.IntegerField(default=0),
        ),
    ]
