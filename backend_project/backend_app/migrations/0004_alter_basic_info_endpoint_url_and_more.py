# Generated by Django 4.2.8 on 2023-12-30 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_app', '0003_alter_basic_info_github_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basic_info',
            name='endpoint_url',
            field=models.URLField(default='https://backend-ninja-tutorials.onrender.com/post'),
        ),
        migrations.AlterField(
            model_name='basic_info',
            name='github_url',
            field=models.URLField(default='https://github.com/thenoblet/backend_ninja'),
        ),
        migrations.AlterField(
            model_name='basic_info',
            name='name',
            field=models.CharField(default='Patrick A. Noblet', max_length=255),
        ),
    ]
