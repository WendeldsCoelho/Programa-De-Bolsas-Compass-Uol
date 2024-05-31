class Passaro:
    def voar(self):
        print("Voando...")
    
    def emitir_som(self):
        raise NotImplementedError("Este método ainda não foi definido pelas subclasses")

class Pato(Passaro):
     def emitir_som(self):
        print("Pato emitindo som...")
        print("Quack Quack")


class Pardal(Passaro):
    def emitir_som(self):
        print("Pardal emitindo som...")
        print("Piu Piu")

if __name__ == "__main__":
    pato = Pato()
    pardal = Pardal()
    
    print("Pato")
    pato.voar()
    pato.emitir_som()

    print("Pardal")
    pardal.voar()
    pardal.emitir_som()