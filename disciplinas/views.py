from disciplinas.models import Disciplina, Aluno, DisciplinaAluno
from disciplinas.filters import DisciplinaFilter, AlunoFilter, DisciplinaAlunoFilter
from disciplinas.serializers import DisciplinaSerializer, AlunoSerializer, DisciplinaAlunoSerializer
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import exception_handler
from rest_framework.decorators import api_view


class DisciplinaList(generics.ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

    def list(self, request):
        try:
            matricula_excluir = request.QUERY_PARAMS['matricula_excluir']
        except:
            matricula_excluir = None

        if matricula_excluir is not None:
            disciplinasDoAluno = DisciplinaAluno.objects.filter(aluno__matricula=matricula_excluir).values_list('disciplina__id', flat=True).order_by('id')
            disciplinas = self.queryset.exclude(id__in=disciplinasDoAluno)
        else:
            disciplinas = self.queryset

        serializer_class = DisciplinaSerializer(disciplinas, many=True)
        return Response(serializer_class.data)


class DisciplinaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


class AlunoList(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class AlunoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class AlunoList(generics.ListAPIView):
    serializer_class = AlunoSerializer
    queryset = Aluno.objects.all()

    def get_queryset(self):
        queryset = Aluno.objects.all()
        matricula = self.request.QUERY_PARAMS.get('matricula', None)
        if matricula is not None:
            queryset = queryset.filter(matricula=matricula)
        return queryset

    def get(self, request, format=None):
        aluno = self.get_queryset()
        serializer_class = AlunoSerializer(aluno, many=True)

        return Response(serializer_class.data)


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


    def post(self, request, *args, **kwargs):
        response = { 'data': {'success': True }}
        try:
            aluno = Aluno.objects.get(matricula=request.DATA['aluno']['matricula'])
            disciplina = Disciplina.objects.get(id=request.DATA['disciplina']['id'])
            notaNova = request.DATA['nota']

            numeroDeIguais = DisciplinaAluno.objects.filter(aluno=aluno, disciplina=disciplina).count()
            if (numeroDeIguais > 0):
                response['data']['success'] = False
            else:
                nota = DisciplinaAluno(aluno=aluno, disciplina=disciplina, nota=notaNova)
                nota.save()
        except:
            response['data']['success'] = False

        return Response(**response)


class DisciplinaAlunoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DisciplinaAluno.objects.all()
    serializer_class = DisciplinaAlunoSerializer

    def update(self, request, pk=None):
        response = { 'data': {'success': True }}
        try:
            self.queryset.filter(id=request.DATA['id']).update(nota=request.DATA['nota'])
        except:
            response = { 'data': {'success': False }}

        return Response(**response)
