# Generated by Django 4.1.5 on 2023-03-03 05:19

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_category_news_caregory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rahbariyat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150, verbose_name='Tolıq atı')),
                ('image', models.ImageField(upload_to='image/rahbariyat/', verbose_name='Súwret')),
                ('role', models.CharField(max_length=100, verbose_name='Lavozm')),
                ('full_information', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'verbose_name': 'Rahbar ',
                'verbose_name_plural': 'Rahbariyatlar',
            },
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='image/gallery/', verbose_name='Súwret'),
        ),
    ]
