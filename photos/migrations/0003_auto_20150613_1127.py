# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20150529_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, null=True, validators=[photos.validators.badwords]),
        ),
        migrations.AlterField(
            model_name='photo',
            name='license',
            field=models.CharField(default=(), max_length=3, choices=[(b'Av2', b'Apache License v2.0'), (b'RIG', b'Copyright'), (b'LEF', b'CopyLeft'), (b'CC', b'Creative Commons')]),
        ),
    ]
