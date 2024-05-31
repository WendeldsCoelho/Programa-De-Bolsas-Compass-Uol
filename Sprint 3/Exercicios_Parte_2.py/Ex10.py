def remover_duplicatas(lista):
    
    conjunto_sem_duplicatas = set(lista)
    
    lista_sem_duplicatas = list(conjunto_sem_duplicatas)
    
    return lista_sem_duplicatas
    
list_a = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']

result = remover_duplicatas(list_a)

print(result)