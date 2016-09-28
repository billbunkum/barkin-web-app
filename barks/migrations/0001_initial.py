# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bark',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=120)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(to='profiles.UserProfile')),
            ],
        ),
    ]
