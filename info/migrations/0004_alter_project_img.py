# Generated by Django 4.0.6 on 2022-07-30 16:06

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_remove_home_discord_remove_home_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='img',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
