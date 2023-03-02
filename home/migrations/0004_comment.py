# Generated by Django 4.1.5 on 2023-02-24 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_nextmatch_kamanda1_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=25, verbose_name='Tolıq atı')),
                ('massage', models.TextField(verbose_name='Xabar')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Xabar waqtı')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='home.news')),
            ],
        ),
    ]
