# Generated by Django 4.1.5 on 2023-02-25 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_player_birth_day_alter_player_full_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='instagram',
            field=models.URLField(blank=True, default='https://www.instagram.com/pfkaral_official/', null=True, verbose_name='Instagram kanal'),
        ),
        migrations.AddField(
            model_name='contact',
            name='telegram',
            field=models.URLField(blank=True, default='https://t.me/Nurlan_Pirjanov', null=True, verbose_name='Telegram kanal'),
        ),
    ]
