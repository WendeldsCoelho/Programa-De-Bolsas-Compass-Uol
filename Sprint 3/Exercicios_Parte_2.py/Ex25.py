class Aviao:
    cor = "azul"
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
    
    def __str__(self):
        return f'O avião de modelo {self.modelo} possui uma velocidade máxima de {self.velocidade_maxima}, capacidade para {self.capacidade} passageiros e é da cor {self.cor}.'
        
aviao1 = Aviao("BOIENG456", "1500 km/h", 400)
aviao2 = Aviao("Embraer Praetor 600", "863 km/h", 14)
aviao3 = Aviao("Antonov An-2", "258 km/h", 12)

avioes = [aviao1, aviao2, aviao3]

for aviao in avioes:
    print(aviao)