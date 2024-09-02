# Generated by Django 4.1.2 on 2022-10-17 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('email_address', models.EmailField(max_length=254)),
                ('works_full_time', models.BooleanField()),
                ('job_level', models.CharField(max_length=20)),
                ('photo', models.URLField()),
                ('birth_date', models.DateField()),
            ],
        ),
    ]
