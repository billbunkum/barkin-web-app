# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('barks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bark',
            name='profile',
        ),
        migrations.AddField(
            model_name='bark',
            name='user',
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
