# Generated by Django 4.2.3 on 2023-07-22 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('delivery', models.TextField(default='Not Delivered')),
            ],
        ),
        migrations.CreateModel(
            name='Prompts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='NULL', max_length=30)),
                ('title', models.TextField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('prompt', models.TextField(max_length=5000)),
                ('price', models.FloatField(default=0.0, max_length=30)),
                ('category', models.TextField(default='normal', max_length=30)),
                ('sample_input', models.TextField(default='null', max_length=10000)),
                ('sample_output', models.TextField(default='null', max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('email', models.TextField(max_length=50)),
                ('password', models.TextField(max_length=10)),
            ],
        ),
    ]
