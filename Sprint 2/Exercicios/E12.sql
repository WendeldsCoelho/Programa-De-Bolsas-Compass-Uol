--Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). 
--As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.
--Observação: Apenas vendas com status concluído.
select
    dependente.cddep,
    dependente.nmdep,
    dependente.dtnasc,
    sum(vendas.qtd * vendas.vrunt) as valor_total_vendas
from tbdependente as dependente
join tbvendedor as vendedor
    on dependente.cdvdd = vendedor.cdvdd
join tbvendas as vendas 
    on vendedor.cdvdd = vendas.cdvdd
where vendas.status = 'Concluído' 
group by dependente.cddep,dependente.nmdep,dependente.dtnasc
having valor_total_vendas != 0
order by valor_total_vendas 
limit 1

