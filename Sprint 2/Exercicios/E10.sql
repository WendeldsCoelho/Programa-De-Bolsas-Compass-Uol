--A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 
--Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.
--As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.
select 
    vendedor.nmvdd as vendedor,
    sum(vendas.qtd * vendas.vrunt) as valor_total_vendas,
    round(sum(vendas.qtd * vendas.vrunt) * (vendedor.perccomissao/100.0),2) as comissao
from tbvendedor as vendedor
left join tbvendas as vendas    
    on vendedor.cdvdd = vendas.cdvdd
where vendas.status = 'Concluído'
group by vendedor.cdvdd
order by comissao desc
