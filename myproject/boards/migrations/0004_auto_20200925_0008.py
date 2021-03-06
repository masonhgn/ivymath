# Generated by Django 3.1 on 2020-09-25 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_postalg_clip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postalg',
            name='videolink',
        ),
        migrations.RemoveField(
            model_name='postcalc',
            name='videolink',
        ),
        migrations.RemoveField(
            model_name='postprec',
            name='videolink',
        ),
        migrations.RemoveField(
            model_name='posttrig',
            name='videolink',
        ),
        migrations.AddField(
            model_name='postcalc',
            name='clip',
            field=models.FileField(null=True, upload_to='user_videos/'),
        ),
        migrations.AddField(
            model_name='postprec',
            name='clip',
            field=models.FileField(null=True, upload_to='user_videos/'),
        ),
        migrations.AddField(
            model_name='posttrig',
            name='clip',
            field=models.FileField(null=True, upload_to='user_videos/'),
        ),
    ]
