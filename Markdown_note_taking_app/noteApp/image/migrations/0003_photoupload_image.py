# Generated by Django 5.0.6 on 2024-06-10 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_remove_photoupload_image_photoupload_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoupload',
            name='image',
            field=models.ImageField(default='default.txt', upload_to='images/'),
            preserve_default=False,
        ),
    ]