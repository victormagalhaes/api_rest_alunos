from django.contrib import admin
from .models import Disciplina, Aluno, DisciplinaAluno

# Register your models here.

admin.site.register(Disciplina)
admin.site.register(Aluno)
admin.site.register(DisciplinaAluno)
