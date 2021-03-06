# Generated by Django 2.0.13 on 2019-02-21 13:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190221_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(related_name='_user_followers_+', to=settings.AUTH_USER_MODEL, verbose_name='followers'),
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(related_name='_user_following_+', to=settings.AUTH_USER_MODEL, verbose_name='following'),
        ),
    ]
