# Generated by Django 5.0.6 on 2024-06-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='order_items',
            field=models.ManyToManyField(to='api.orderitem'),
        ),
    ]
