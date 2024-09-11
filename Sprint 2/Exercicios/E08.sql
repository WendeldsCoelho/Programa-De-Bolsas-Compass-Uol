--Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída. 
select
    vendedor.cdvdd,
    vendedor.nmvdd
from tbvendedor as vendedor
left join tbvendas  as vendas
    on vendedor.cdvdd = vendas.cdvdd
group by vendedor.cdvdd, vendedor.nmvdd
order by count(vendas.status = 'Concluído') desc
limit 1