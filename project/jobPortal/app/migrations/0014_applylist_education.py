# Generated by Django 5.1.4 on 2025-01-19 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_company_description_alter_company_logo_pic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applylist',
            name='education',
            field=models.CharField(default='', max_length=200),
        ),
    ]