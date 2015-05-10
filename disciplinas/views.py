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
        import ipdb; ipdb.set_trace()

        response = { 'data': {'success': True }}

        aluno_id = request.DATA['aluno_id']
        disciplina_id = request.DATA['disciplina_id']

        if (request.DATA['metodo'] == 'alterar'):
            nota_atualizada = request.DATA['nota']
            try:
                DisciplinaAluno.objects.filter(aluno__id=aluno_id, disciplina__id=disciplina_id).update(nota=nota_atualizada)
            except:
                response['data']['success'] = False
        elif (request.DATA['metodo'] == 'excluir'):
            try:
                DisciplinaAluno.objects.filter(aluno__id=aluno_id, disciplina__id=disciplina_id).delete()
            except:
                response['data']['success'] = False

        return Response(**response)

class DisciplinaAlunoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DisciplinaAluno.objects.all()
    serializer_class = DisciplinaAlunoSerializer

    def update(self, request, pk=None):
        response = { 'data': {'success': True }}
        try:
            import ipdb; ipdb.set_trace()

            self.queryset.filter(id=request.DATA['id']).update(nota=request.DATA['nota'])
        except:
            response = { 'data': {'success': False }}

        return Response(**response)
