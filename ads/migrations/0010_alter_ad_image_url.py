# Generated by Django 5.2 on 2025-04-10 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0009_merge_20250409_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='ad/'),
        ),
    ]
