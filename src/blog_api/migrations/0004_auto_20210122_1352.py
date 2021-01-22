# Generated by Django 3.1.5 on 2021-01-22 10:52

import blog_api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0003_auto_20210122_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.RemoveField(
            model_name='postview',
            name='post',
        ),
        migrations.RemoveField(
            model_name='postview',
            name='user',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='dnz-security.png', upload_to=blog_api.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Publised')], default='d', max_length=10),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='PostView',
        ),
    ]
