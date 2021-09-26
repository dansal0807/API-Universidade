from django.contrib import admin
from Escola.models import Aluno, Curso, Matricula


#Aqui são apresentadas as informações do Super usuário do django, para fácil cadastramento.
class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg','cpf','data_nascimento')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_per_page = 20

#Note como é usada a base do Models para fazer esse display no django admin.
admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id','codigo_curso','descricao')
    list_display_links = ('id','codigo_curso')
    search_fields = ('codigo_curso', )

admin.site.register(Curso, Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id','aluno','curso', 'periodo')
    list_display_links = ('id',)

admin.site.register(Matricula, Matriculas)


