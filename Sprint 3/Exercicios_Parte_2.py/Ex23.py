class Calculo:
    def soma(self,x,y):
        result = x + y
        return result
    def subtracao(self,x,y):
        result = x - y
        return result

x = 4
y = 5

calculo = Calculo()

resultado_soma = calculo.soma(x,y)
resultado_subtracao = calculo.subtracao(x,y)

print(f"Somando: {x}+{y} = {resultado_soma}")
print(f"Subtraindo: {x}-{y} = {resultado_subtracao}")