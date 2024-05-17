--Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída.
-- As colunas presentes no resultado devem ser cdpro e nmpro.
select
    produto.cdpro,
    vendas.nmpro
from tbestoqueproduto as produto
left join tbvendas as vendas
    on produto.cdpro = vendas.cdpro
where vendas.dtven between '2014-02-03 00:00:00' and '2018-02-03 00:00:00' and vendas.status = 'Concluído'
group by produto.cdpro, vendas.nmpro
order by count(vendas.qtd) desc
limit 1
