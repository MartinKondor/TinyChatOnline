# Generated by Django 4.2.11 on 2024-03-22 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiv1', '0006_remove_usersettings_account_deactivation_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersettings',
            name='block_users',
        ),
        migrations.AlterField(
            model_name='usersettings',
            name='blocked_words',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='usersettings',
            name='block_users',
            field=models.TextField(default=''),
        ),
    ]
