# Generated by Django 3.2.8 on 2021-10-28 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20211028_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='isOwner',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
