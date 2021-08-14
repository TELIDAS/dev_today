# Generated by Django 3.2.6 on 2021-08-14 11:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news_board', '0008_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='votes',
            field=models.ManyToManyField(related_name='blogpost', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
