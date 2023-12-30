# Generated by Django 4.2.8 on 2023-12-30 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic_info',
            name='github_url',
            field=models.URLField(default='https://github.com/thenoblet'),
        ),
        migrations.AlterField(
            model_name='basic_info',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
