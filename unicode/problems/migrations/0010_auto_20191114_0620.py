# Generated by Django 2.2.5 on 2019-11-14 06:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('problems', '0009_auto_20191113_1850'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='upvote',
            unique_together={('problem', 'user')},
        ),
    ]