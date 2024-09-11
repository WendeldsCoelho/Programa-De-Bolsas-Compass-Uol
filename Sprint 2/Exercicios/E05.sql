--Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil.
--Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.
select distinct 
    aut.nome
from autor as aut
join livro as liv on aut.codAutor = liv.autor
join editora as edi on liv.editora = edi.codEditora
join endereco as end on edi.endereco = end.codEndereco
where end.estado not in ('PARANÁ', 'RIO GRANDE DO SUL', 'SANTA CATARINA')
order by aut.nome
