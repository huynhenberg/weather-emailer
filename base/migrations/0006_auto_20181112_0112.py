# Generated by Django 2.1.2 on 2018-11-12 01:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_user_last_modified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='activation_date',
        ),
        migrations.AddField(
            model_name='user',
            name='activation_datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
