# Generated by Django 4.1.2 on 2023-04-14 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_post_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumb',
            field=models.ImageField(null=True, upload_to='media/post_img/%Y/%m/%d'),
        ),
    ]