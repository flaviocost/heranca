class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f'{self.nome} está comendo......')

    def emitirsom(self):
        print()
class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)

    def emitirsom(self):
        print(f'{self.nome} está miandoo......')

class Vaca(Animal):
    def __init__(self,nome, cor):
        super().__init__(nome, cor)

    def emitirsom(self):
        print(f'{self.nome} está mugindo......')

    def dormindo(self):
        print(f'{self.nome} dormindo....')
class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitirsom(self):
        print(f'{self.nome} está Rosnando......')

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def emitirsom(self):
        print(f'{self.nome} está latindo......')

    def dormindo(self):
        print(f'{self.nome} dormindo....')

