from functools import reduce

def calcula_saldo(lancamentos) -> float:
    #continue este código
    valores = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)
    
    valor_final = reduce(lambda saldo, x: saldo + x, valores)
    
    return valor_final
    
lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]

print(calcula_saldo(lancamentos))