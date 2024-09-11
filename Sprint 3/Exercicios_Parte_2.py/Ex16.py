def soma(numeros_str):
    
    numeros_lista = numeros_str.split(',')
    
    numeros_inteiros = [int(numero) for numero in numeros_lista]
    
    result = sum(numeros_inteiros)
    
    return result

numeros = "1,3,4,6,10,76"

resultado = soma(numeros)

print(resultado)