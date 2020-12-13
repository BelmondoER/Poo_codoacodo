import random


class Cliente2:

    cuentasSuspendidas = []

    def __init__(self, codigo, nombre):
        self.codigo = codigo
        self.nombre = nombre

    def __str__(self):
        print()
        texto =f'El cliente {self.nombre} tiene su cuenta {self.suspender()}'
        return texto

    def suspender(self):
        if random.randint(0, 1):
            Cliente2.cuentasSuspendidas.append(self.codigo)
            cadena = "suspendida"
        else:
            cadena = "habilitada"
        return cadena