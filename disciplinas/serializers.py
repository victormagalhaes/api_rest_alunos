from django.forms import widgets
from rest_framework import serializers
from disciplinas.models import Disciplina, Aluno, DisciplinaAluno

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno

class DisciplinaAlunoSerializer(serializers.ModelSerializer):
    aluno = AlunoSerializer()
    disciplina = DisciplinaSerializer()

    class Meta:
        model = DisciplinaAluno
