# Generated by Django 3.2.15 on 2022-08-19 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
    ]
