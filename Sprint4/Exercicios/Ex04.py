def calcular_valor_maximo(operadores,operandos) -> float:
    
    operacoes = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '%': lambda x, y: x % y
    }
    
    resultado = list(map(lambda valores: operacoes[valores[0]](valores[1][0],valores[1][1]), zip(operadores,operandos)))
    
    maior_valor = max(resultado)
    
    return maior_valor

operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

print(calcular_valor_maximo(operadores,operandos))