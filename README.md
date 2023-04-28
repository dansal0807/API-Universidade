# University-API

The purpose of this project is to implement the concepts learned through Clean Architecture. Additionally, it aims to present models and relationships between models in the REST model. My intention was to present a project that relates these concepts in a clear and explicit way.

Regarding the project itself:

We have two major models: Courses and Students. We also have enrollments, which serve as a way of relating courses and students. In addition to being able to view, modify, and add courses and students to our database, we can relate the two fields precisely through enrollments.

Thus, we can view the students enrolled in a specific course:

Course X:

student 1
student 2
student 3
And so on.

Likewise, we can also view the courses in which a specific student is enrolled:

Student X:

course 1
course 2
course 3
And so on.

If you wish to use the code on your machine, you need to instantiate a virtual environment, have Python installed, and install the djangorestframework package. After installation, you need to use the command "py manage.py runserver" on the terminal (for Windows, for Linux and Mac, use Python instead of py).


# API-Universidade

Este projeto tem por intuito a implementação dos conceitos apreendidos pelo Clean Architecture. Além disso, ele busca apresenta modelos e relações entre modelos no modelo REST.
Meu intuito foi fazer uma apresentação de um projeto que relacione estes conceitos de uma forma clara e explicita. 

Quanto ao projeto em si:

Temos dois grandes modelos: Cursos e Alunos.
Também possuímos as matrículas, que funcionam como uma forma de relacionar os cursos e os alunos. Além de podermos visualizar, modificar e acrescentar cursos e alunos ao nosso banco de dados, podemos
relacionar os dois campos a partir, justamente, das matrículas. 

Assim, podemos visualizar os alunos inscritos de um curso determinado:

Curso X:
 - aluno 1
 - aluno 2
 - aluno 3
 
E assim em diante.

Da mesma forma, também podemos visualizar os cursos que um aluno determinado está inscrito:

Aluno X:
 - curso 1
 - curso 2
 - curso 3
 
E assim em diante.

- Caso deseje utilizar o código em sua máquina, você necessita instanciar um ambiente virtual, estar com o python baixado e instalar o pacote djangorestframework. Após ser instalado, é preciso utilizar o comando "py manage.py runserver" no terminal (para o windows, para Linux e Mac, utiliza python ao invés de py).

