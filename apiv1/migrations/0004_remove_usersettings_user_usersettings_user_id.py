# Generated by Django 4.2.11 on 2024-03-22 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiv1', '0003_usersettings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersettings',
            name='user',
        ),
        migrations.AddField(
            model_name='usersettings',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
