# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disciplinas', '0003_auto_20150423_0207'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisciplinaAluno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nota', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='disciplinas',
        ),
        migrations.RemoveField(
            model_name='disciplina',
            name='nota',
        ),
        migrations.AddField(
            model_name='disciplinaaluno',
            name='aluno',
            field=models.ForeignKey(to='disciplinas.Aluno'),
        ),
        migrations.AddField(
            model_name='disciplinaaluno',
            name='disciplinas',
            field=models.ManyToManyField(to='disciplinas.Disciplina'),
        ),
    ]
