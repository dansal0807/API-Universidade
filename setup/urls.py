from django.contrib import admin
from django.urls import path, include
from Escola.views import AlunosViewSet, CursosViewSet, ListaAlunosMatriculados, MatriculasViewSet,ListaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename = 'Alunos')
router.register('cursos', CursosViewSet, basename = 'Cursos')
router.register('matriculas', MatriculasViewSet, basename = 'Matriculas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas/', ListaViewSet.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view())
]
