# Generated by Django 2.2.5 on 2019-10-28 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersubmission',
            old_name='solution',
            new_name='submission',
        ),
        migrations.RenameField(
            model_name='usersubmission',
            old_name='submitted',
            new_name='submitter',
        ),
    ]
