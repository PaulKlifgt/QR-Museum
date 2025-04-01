# Generated by Django 5.1.7 on 2025-04-01 06:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_exhibit_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('template', models.IntegerField(choices=[(1, 'Корабль'), (2, 'Археолог'), (3, 'Копатель')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('correct', models.CharField(max_length=200)),
                ('uncorrect_1', models.CharField(max_length=200)),
                ('uncorrect_2', models.CharField(max_length=200)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.game')),
            ],
        ),
    ]
