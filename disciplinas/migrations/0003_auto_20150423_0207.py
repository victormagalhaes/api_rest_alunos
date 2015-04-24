# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disciplinas', '0002_aluno_disciplinas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='disciplina',
            name='nota',
            field=models.CharField(max_length=200),
        ),
    ]
