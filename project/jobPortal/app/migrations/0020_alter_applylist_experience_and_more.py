# Generated by Django 5.1.4 on 2025-01-19 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_jobdetails_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applylist',
            name='experience',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='experience',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
