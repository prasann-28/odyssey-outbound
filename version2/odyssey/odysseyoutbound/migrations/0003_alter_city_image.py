# Generated by Django 4.1 on 2024-04-13 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odysseyoutbound', '0002_city_destination_cities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='image',
            field=models.CharField(max_length=100),
        ),
    ]
