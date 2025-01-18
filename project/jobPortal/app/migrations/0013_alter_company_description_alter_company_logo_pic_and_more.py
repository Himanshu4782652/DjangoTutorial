# Generated by Django 5.1.4 on 2025-01-18 08:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_company_description_alter_company_logo_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo_pic',
            field=models.ImageField(default='', upload_to='app/img/company'),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='company_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.company'),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='companyaddress',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='companycontact',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='companyemail',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='companyname',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='companywebsite',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='experience',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='jobdescription',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='jobname',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='location',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='logo',
            field=models.ImageField(default='', upload_to='app/img/jobpost'),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='qualification',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='responsibities',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='jobdetails',
            name='salarypackage',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.CreateModel(
            name='ApplyList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_salary', models.CharField(max_length=200)),
                ('max_salary', models.CharField(max_length=200)),
                ('resume', models.FileField(upload_to='app/resume')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.candidate')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.jobdetails')),
            ],
        ),
    ]