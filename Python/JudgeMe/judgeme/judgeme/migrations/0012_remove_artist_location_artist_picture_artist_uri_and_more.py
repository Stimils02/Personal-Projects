# Generated by Django 4.1.2 on 2022-11-16 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judgeme', '0011_merge_20221104_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='location',
        ),
        migrations.AddField(
            model_name='artist',
            name='picture',
            field=models.CharField(default='a', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artist',
            name='uri',
            field=models.CharField(default='a', max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jmuser',
            name='top_artists',
            field=models.ManyToManyField(blank=True, to='judgeme.artist'),
        ),
    ]