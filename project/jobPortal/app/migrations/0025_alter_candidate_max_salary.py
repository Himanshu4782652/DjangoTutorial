# Generated by Django 5.1.4 on 2025-04-10 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_alter_candidate_min_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='max_salary',
            field=models.BigIntegerField(default=''),
        ),
    ]
