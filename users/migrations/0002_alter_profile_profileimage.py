# Generated by Django 3.2.8 on 2021-10-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileImage',
            field=models.ImageField(blank=True, default='images/user/user-default.png', null=True, upload_to='images/user/'),
        ),
    ]
