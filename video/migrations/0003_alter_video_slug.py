# Generated by Django 5.0.4 on 2024-04-17 23:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("video", "0002_remove_video_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="slug",
            field=models.SlugField(unique=True, verbose_name="URL Slug"),
        ),
    ]
