# Generated by Django 3.1 on 2020-12-05 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='realese_date',
            new_name='release_date',
        ),
    ]
