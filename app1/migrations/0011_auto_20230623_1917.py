# Generated by Django 3.2.18 on 2023-06-23 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0010_remove_workspace_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workspace',
            name='member1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workspace_member1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='member2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workspace_member2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='member3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workspace_member3', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='member4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workspace_member4', to=settings.AUTH_USER_MODEL),
        ),
    ]
