# Generated by Django 5.1.4 on 2025-01-19 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_applylist_experience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdetails',
            name='experience',
            field=models.IntegerField(),
        ),
    ]
