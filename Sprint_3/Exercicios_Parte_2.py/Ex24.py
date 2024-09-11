class Ordenadora:
    
    def __init__(self, lista):
        self.listaBaguncada = lista
    
    def ordenacaoCrescente(self):
        result = sorted(self.listaBaguncada)
        return result
        
    def ordenacaoDecrescente(self):
        result = sorted(self.listaBaguncada, reverse=True)
        return result

crescente = Ordenadora([3,4,2,1,5])
decrescente = Ordenadora([9,7,6,8])

lista_ordenada_crescente = crescente.ordenacaoCrescente()
lista_ordenada_decrescente = decrescente.ordenacaoDecrescente()

print(lista_ordenada_crescente)
print(lista_ordenada_decrescente)
