# Generated by Django 4.1.5 on 2023-03-07 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_delete_match_oldmatch_full_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oldmatch',
            name='kamanda1',
        ),
        migrations.RemoveField(
            model_name='oldmatch',
            name='kamanda2',
        ),
    ]
