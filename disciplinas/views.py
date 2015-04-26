from disciplinas.models import Disciplina, Aluno, DisciplinaAluno
from disciplinas.filters import DisciplinaFilter, AlunoFilter, DisciplinaAlunoFilter
from disciplinas.serializers import DisciplinaSerializer, AlunoSerializer, DisciplinaAlunoSerializer
from rest_framework.response import Response
from rest_framework import generics


class DisciplinaList(generics.ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class DisciplinaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class AlunoList(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class AlunoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class DisciplinaAlunoList(generics.ListAPIView):
    serializer_class = DisciplinaAlunoSerializer
    queryset = DisciplinaAluno.objects.all()

    def get_queryset(self):
        queryset = DisciplinaAluno.objects.all()
        aluno = self.request.QUERY_PARAMS.get('aluno', None)
        if aluno is not None:
            queryset = queryset.filter(aluno__matricula=aluno)
        return queryset

    def get(self, request, format=None):
        notas = self.get_queryset()
        serializer_class = DisciplinaAlunoSerializer(notas, many=True)

        return Response(serializer_class.data)


    def post(self, request, format=None):
        serializer_class = DisciplinaAlunoSerializer(data=request.DATA)
        if serializer_class.is_valid():
          serializer_class.save()
          return Response(serializer_class.data, status=status.HTTP_201_CREATED)
        else:
          return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class DisciplinaAlunoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DisciplinaAluno.objects.all()
    serializer_class = DisciplinaAlunoSerializer
