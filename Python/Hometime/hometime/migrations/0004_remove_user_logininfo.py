# Generated by Django 4.1.1 on 2022-12-04 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hometime', '0003_user_logininfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='loginInfo',
        ),
    ]
