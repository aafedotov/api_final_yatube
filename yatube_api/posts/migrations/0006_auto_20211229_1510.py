# Generated by Django 2.2.16 on 2021-12-29 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20211229_1508'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_follow',
        ),
    ]