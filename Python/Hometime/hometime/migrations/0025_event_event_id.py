# Generated by Django 4.1.1 on 2022-12-09 23:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('hometime', '0024_remove_event_event_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, null=True),
        ),
    ]
