# Generated by Django 4.1.1 on 2022-12-06 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hometime', '0009_user_friends'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friends', models.ManyToManyField(blank=True, to='hometime.user')),
            ],
        ),
    ]
