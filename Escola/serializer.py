from rest_framework import serializers
from Escola.models import Aluno, Curso, Matricula

#Este arquivo é o grande diferencial do Django tradicional para o REST.
#O serializer é um transformador de JSON para o formato dicionário que facilita essa transição para nós, desenvolvedores.
#Note como seu princípio são as bases do models.

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id','nome','rg','cpf','data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

 #aqui estão as matrículas (de um curso) de um aluno;
 #aluno x: curso 1, curso 2, curso 3...
class MatriculasListadasSerializer(serializers.ModelSerializer):
    curso=serializers.ReadOnlyField(source='curso.descricao')
    periodo=serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()

#aqui estão as matrículas dos alunos matriculados em um determinado curso;
#curso x: aluno 1, aluno 2, aluno 3...
class AlunosMatriculadosListaSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']