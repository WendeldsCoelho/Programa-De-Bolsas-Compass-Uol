def conta_vogais(texto:str)-> int:
    vogais = 'AEIOUaeiou'
    
    lista_vogais = list(filter(lambda char: char in vogais, texto))
    
    return len(lista_vogais)
    
print(conta_vogais("Testando a função"))