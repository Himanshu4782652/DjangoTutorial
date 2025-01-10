# Generated by Django 5.1.4 on 2025-01-09 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_candidate_country_candidate_experience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='country',
            field=models.CharField(default=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='experience',
            field=models.CharField(default=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='highestedu',
            field=models.CharField(default=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='job_type',
            field=models.CharField(default=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='jobcategory',
            field=models.CharField(default=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='jobdescription',
            field=models.CharField(default=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='max_salary',
            field=models.BigIntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='min_salary',
            field=models.BigIntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='shift',
            field=models.CharField(default=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='website',
            field=models.CharField(default=True, max_length=150),
        ),
    ]
