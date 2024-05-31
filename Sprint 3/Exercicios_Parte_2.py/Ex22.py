class Pessoa:
    def __init__(self, id):
        self.id = id
        self.__nome = None
    
    #método para retornar o valor do atributo
    def nome(self):
        return self.__nome
    
    #método para definir o valor de __nome
    def nome(self, nome):
        self.__nome = nome
        
pessoa = Pessoa(0)
pessoa.nome = 'Fulano De Tal'
print(pessoa.nome)