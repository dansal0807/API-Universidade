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
 
E assim em diante...

Da mesma forma, também podemos visualizar os cursos que um aluno determinado está inscrito:

Aluno X:
 - curso 1
 - curso 2
 - curso 3
 
E assim em diante...
