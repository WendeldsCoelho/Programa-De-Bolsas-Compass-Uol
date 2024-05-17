--Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.
select 
    aut.nome
from autor as aut
left join livro as liv
    on aut.codAutor = liv.autor
group by aut.nome
having count(liv.cod) = 0 
order by aut.nome