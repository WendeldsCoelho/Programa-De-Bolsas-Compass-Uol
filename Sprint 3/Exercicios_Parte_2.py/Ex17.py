def subdivision(lista):
    n = len(lista)
    section = n//3
    
    parte1 = lista[:section]
    parte2 = lista[section:section*2]
    parte3 = lista[section*2:]
    
    result =f"{parte1} {parte2} {parte3}"
    
    return result

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

resultado = subdivision(lista)

print(resultado)