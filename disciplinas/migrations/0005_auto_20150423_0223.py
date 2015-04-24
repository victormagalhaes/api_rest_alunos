# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disciplinas', '0004_auto_20150423_0213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplinaaluno',
            name='disciplinas',
        ),
        migrations.AddField(
            model_name='disciplinaaluno',
            name='disciplina',
            field=models.ForeignKey(default=1, to='disciplinas.Disciplina'),
            preserve_default=False,
        ),
    ]
