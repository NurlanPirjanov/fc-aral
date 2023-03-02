# Generated by Django 4.1.5 on 2023-02-15 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_logofc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nextmatch',
            name='kamanda1_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nextkam1', to='home.logofc'),
        ),
        migrations.AlterField(
            model_name='nextmatch',
            name='kamanda2_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nextkam2', to='home.logofc'),
        ),
        migrations.AlterField(
            model_name='oldmatch',
            name='kamanda1_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kam1', to='home.logofc'),
        ),
        migrations.AlterField(
            model_name='oldmatch',
            name='kamanda2_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kam2', to='home.logofc'),
        ),
    ]
