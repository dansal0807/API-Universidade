from rest_framework import viewsets, generics
from Escola.models import Aluno, Curso, Matricula
from Escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, MatriculasListadasSerializer, AlunosMatriculadosListaSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

#A view é a grande apresentação de todos os dados reunidos. Aqui se fazem as relações entre Models e as URLs.
#Note como "puxamos" tanto o models quanto o serializer aqui; isto indica a 'junção' entre estes dois elementos.
#Aqui também é onde se "puxa" o serializer que será encaminhado para as URLs.

class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os alunos e alunas """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    #Abaixo colocarei a autenticação da API na seção de Alunos:
    authentication_class = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os cursos """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    #Abaixo colocarei a autenticação da API na seção de Cursos:
    authentication_class = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculasViewSet(viewsets.ModelViewSet):
    """ Listando todas as matrículas """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    #Abaixo colocarei a autenticação da API na seção de Matriculas:
    authentication_class = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaViewSet(generics.ListAPIView):
    """ Listando as matrículas de um aluno ou aluna"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk']) #aluno_id é uma variável criada, em que busca da classe Matrcula a pk (primary key)
        return queryset
    serializer_class = MatriculasListadasSerializer
    #Abaixo colocarei a autenticação da API na seção das matrículas (de um curso) de um aluno:
    authentication_class = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaAlunosMatriculados(generics.ListAPIView):
    """ Listando alunos matriculados em um curso """
    def get_queryset(self):
        queryset= Matricula.objects.filter(curso_id = self.kwargs['pk']) #curso_id é uma variável criada, em que busca da classe Matrcula a pk (primary key)
        return queryset
    serializer_class = AlunosMatriculadosListaSerializer
    #Abaixo colocarei a autenticação da API na seção dos alunos matriculados em um curso:
    authentication_class = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
