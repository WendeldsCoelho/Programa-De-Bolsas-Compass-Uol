def my_map(lista, f):
    result = []
    
    for elemento in lista:
        result.append(f(elemento))
        
    return result

def potencia_2(x):
    return x ** 2

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = my_map(lista, potencia_2)

print(result)