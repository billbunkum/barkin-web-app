# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='getUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, primary_key=True, to=settings.AUTH_USER_MODEL, auto_created=True, serialize=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
