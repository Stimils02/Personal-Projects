# Generated by Django 4.1.1 on 2022-11-30 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judgeme', '0021_alter_jmuser_uploaded_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='uploaded_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
