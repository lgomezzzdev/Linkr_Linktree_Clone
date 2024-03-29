# Generated by Django 3.2.8 on 2021-10-28 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211027_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='isAdmin',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='isDonator',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='isNewUser',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='isSuperDonator',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
