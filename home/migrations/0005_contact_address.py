# Generated by Django 4.1.5 on 2023-02-25 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.CharField(default='Adress', max_length=200, verbose_name='Mánzil'),
        ),
    ]
