# Generated by Django 4.1.1 on 2022-12-06 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hometime', '0011_remove_friend_friends_friend_friend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='friends',
        ),
    ]