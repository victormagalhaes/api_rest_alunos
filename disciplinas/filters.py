from disciplinas.models import Disciplina, Aluno, DisciplinaAluno
import django_filters

class DisciplinaFilter(django_filters.FilterSet):
    class Meta:
        model = Disciplina
        fields = ['id']


class AlunoFilter(django_filters.FilterSet):
    class Meta:
        model = Aluno
        fields = ['id']


class DisciplinaAlunoFilter(django_filters.FilterSet):
    class Meta:
        model = DisciplinaAluno
        fields = ['id']
