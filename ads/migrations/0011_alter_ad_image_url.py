# Generated by Django 5.2 on 2025-04-10 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0010_alter_ad_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
