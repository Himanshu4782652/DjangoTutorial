# Generated by Django 5.1.4 on 2025-01-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_applylist_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applylist',
            name='experience',
            field=models.IntegerField(default=0),
        ),
    ]
