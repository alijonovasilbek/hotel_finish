# Generated by Django 5.1.1 on 2024-09-29 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sativa', '0002_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='rooms',
            field=models.CharField(max_length=10),
        ),
    ]
