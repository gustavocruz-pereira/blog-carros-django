# Generated by Django 4.1.2 on 2023-03-30 23:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_post_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='thumb',
            field=models.ImageField(blank=True, null=True, upload_to='post_img/%Y/%m/%d'),
        ),
    ]
