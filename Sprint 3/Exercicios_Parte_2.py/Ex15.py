class Lampada:
    def __init__(self, estado: bool):
        self.ligada = estado
    
    def liga(self):
        self.ligada = True
        
    def desliga(self):
        self.ligada = False
        
    def esta_ligada(self):
        return self.ligada

lp = Lampada(False)  
lp.liga()
print("A lâmpada está ligada?", lp.esta_ligada())
lp.desliga()
print("A lâmpada ainda está ligada?", lp.esta_ligada())