# Generated by Django 3.2.18 on 2023-06-23 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_alter_workspace_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workspace',
            name='user',
        ),
    ]
