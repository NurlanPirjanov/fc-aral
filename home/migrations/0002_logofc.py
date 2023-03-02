# Generated by Django 4.1.5 on 2023-02-15 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogoFc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Kamanda atı')),
                ('img', models.ImageField(upload_to='images/logo/', verbose_name='Kamanda logosı')),
            ],
            options={
                'verbose_name': 'Kamanda logotipi',
                'verbose_name_plural': 'Kamanda logotipleri',
            },
        ),
    ]