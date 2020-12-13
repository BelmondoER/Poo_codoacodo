class Cliente:

    def __init__(self, nombre):
        self.nombre = nombre
        self.monto = 0

    def depositar(self):
        self.monto += float(input(f"{self.nombre} Ingrese dinero : >>>"))

    def extraer(self):
        self.monto -= float(input(f"{self.nombre} Tiene para extraer {self.monto} : >>>"))

    def retornar_monto(self):
        return self.monto

class Banco:

    cliente1 = Cliente("Jose")
    cliente2 = Cliente("Ana")
    cliente3 = Cliente("Francisco")

    def __init__(self, nombre):
        self.total = 0
        self.nombre = nombre

    def operar(self):
        self.cliente1.depositar()
        self.cliente2.depositar()
        self.cliente3.depositar()

        self.cliente1.extraer()
        self.cliente2.extraer()
        self.cliente3.extraer()

    def contabilizar_acumulado(self):
        self.total += self.cliente1.retornar_monto()
        self.total += self.cliente2.retornar_monto()
        self.total += self.cliente3.retornar_monto()
        return self.total

    def __str__(self):
        estring = f'El dinero depositado en el Banco {self.nombre} al final del dia es {self.contabilizar_acumulado()}'
        return estring

