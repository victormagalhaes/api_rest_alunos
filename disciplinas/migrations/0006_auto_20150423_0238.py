# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disciplinas', '0005_auto_20150423_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplinaaluno',
            name='aluno',
            field=models.ForeignKey(related_name='aluno_matricula', to='disciplinas.Aluno'),
        ),
        migrations.AlterField(
            model_name='disciplinaaluno',
            name='disciplina',
            field=models.ForeignKey(related_name='disciplina_nome', to='disciplinas.Disciplina'),
        ),
    ]
