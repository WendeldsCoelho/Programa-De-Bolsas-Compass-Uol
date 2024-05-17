--Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade.
--Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.
select 
    count(liv.cod) as quantidade,
    edi.nome,
    end.estado,
    end.cidade
from editora as edi
left join livro as liv
    on edi.codEditora = liv.editora
left join endereco as end
    on edi.endereco = end.codEndereco
group by edi.codEditora
having quantidade > 0
order by quantidade desc 
limit 5