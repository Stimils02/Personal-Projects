# Generated by Django 4.1.1 on 2022-11-04 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judgeme', '0006_jmuser_about_jmuser_vibes'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='picture',
            field=models.CharField(default='aaa', max_length=256),
            preserve_default=False,
        ),
    ]