import random


class Dado:

    def __init__(self):
        self.caras = 6
        self.valor = 1

    def tirar(self):
        self.valor = random.randint(1, self.caras)

    def imprimir(self):
        print(f'El numero de el dado es {self.retornar_valor()}')

    def retornar_valor(self):
        return self.valor


class JuegoDeDados:

    dado1 = Dado()
    dado2 = Dado()
    dado3 = Dado()

    def __init__(self):
        tecla = "s"
        while tecla != "n":
            print()
            self.intento = input("Presione ENTER para lanzar los dados ")
            print()
            self.jugar()
            tecla = input("Desea seguir intentando? --- s/n : ")
        print()
        print("Hasta la proxima")

    def jugar(self):
        self.dado1.tirar()
        self.dado2.tirar()
        self.dado3.tirar()
        self.dado1.imprimir()
        self.dado2.imprimir()
        self.dado3.imprimir()
        if self.dado1.retornar_valor() == self.dado2.retornar_valor() \
                and self.dado2.retornar_valor() == self.dado3.retornar_valor():
            print(" GANASTE ")
        else:
            print()
            print(" Lo siento mucho, la proxima vez sera ")
            print()
