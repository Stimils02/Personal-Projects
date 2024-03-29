# Generated by Django 4.1.1 on 2022-12-13 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hometime', '0031_event_hometime_ev_day_067bd2_idx'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='event',
            name='hometime_ev_day_067bd2_idx',
        ),
        migrations.AddIndex(
            model_name='event',
            index=models.Index(fields=['event_id'], name='hometime_ev_event_i_7af2be_idx'),
        ),
        migrations.AddIndex(
            model_name='event',
            index=models.Index(fields=['day'], name='hometime_ev_day_499b59_idx'),
        ),
        migrations.AddIndex(
            model_name='friend',
            index=models.Index(fields=['friendUserName'], name='hometime_fr_friendU_45693f_idx'),
        ),
        migrations.AddIndex(
            model_name='user',
            index=models.Index(fields=['username'], name='hometime_us_usernam_29583e_idx'),
        ),
    ]
