# Generated by Django 4.2.3 on 2023-07-25 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mps_app', '0009_prompts_user_alter_users_prompts'),
    ]

    operations = [
        migrations.AddField(
            model_name='prompts',
            name='cost',
            field=models.IntegerField(default=29),
        ),
        migrations.AddField(
            model_name='users',
            name='total_earned',
            field=models.IntegerField(default=0),
        ),
    ]
