# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barks', '0002_auto_20160929_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bark',
            name='content',
            field=models.CharField(max_length=60),
        ),
    ]
