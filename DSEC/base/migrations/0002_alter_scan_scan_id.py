# Generated by Django 5.1.7 on 2025-04-09 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='scan_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
