# Generated by Django 4.2.3 on 2023-07-07 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mps_app', '0003_sellers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('email', models.TextField(max_length=50)),
                ('password', models.TextField(max_length=10)),
            ],
        ),
    ]