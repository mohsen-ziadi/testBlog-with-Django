# Generated by Django 4.1.3 on 2022-11-03 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_publish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish',)},
        ),
    ]