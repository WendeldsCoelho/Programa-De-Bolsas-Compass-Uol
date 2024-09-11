--Apresente a query para listar o autor com maior número de livros publicados.
-- O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.
select 
    aut.codAutor,
    aut.nome,
    count(cod) as quantidade_publicacoes
from autor as aut
left join livro as liv
    on aut.codAutor = liv.autor
group by liv.autor
order by quantidade_publicacoes desc
limit 1