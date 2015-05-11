from django.db import models

# Create your models here.

class Disciplina(models.Model):
    nome = models.CharField(max_length=200)
    carga_horaria = models.IntegerField()

    class Meta:
        ordering = ('nome',)

    def __unicode__(self):
        return self.nome


class Aluno(models.Model):
    matricula = models.CharField(max_length=200)

    def __unicode__(self):
        return self.matricula


class DisciplinaAluno(models.Model):
    aluno = models.ForeignKey(Aluno, related_name='aluno_matricula')
    disciplina = models.ForeignKey(Disciplina, related_name='disciplina_nome')
    nota = models.CharField(max_length=200)

    def __unicode__(self):
        return u'Aluno: %s - Disciplina: %s' % (self.aluno.matricula, self.disciplina.nome)

    class Meta:
        unique_together = ('aluno', 'disciplina')
