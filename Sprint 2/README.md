## Exercicios 
E01
Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas.  Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma.

query.sql ->
select cod, titulo, autor, editora, valor, publicacao, edicao, idioma
from livro
where publicacao > '2014-12-31'
order by cod 

## Evidências


## Certificados

![Curso SQL](https://github.com/WendeldsCoelho/Programa-De-Bolsas-Compass-Uol/blob/main/assets/img/Sprint%202/Certificado_SQL.jpeg?raw=true)

## Desafio

