# Generated by Django 4.1.1 on 2022-12-08 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hometime', '0013_user_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myfriends', to='hometime.user'),
        ),
    ]