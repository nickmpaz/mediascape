# Generated by Django 2.2.8 on 2019-12-14 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_comment_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]