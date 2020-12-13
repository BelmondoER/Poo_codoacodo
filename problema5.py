class Operaciones:

    def __init__(self):
        self.entero1 = int(input('Ingrese el primer entero : '))
        self.entero2 = int(input('Ingrese el segundo entero: '))
        self.sumar()
        self.restar()
        self.dividir()
        self.multiplicar()

    def sumar(self):
        suma = self.entero1 + self.entero2
        print(f'La suma da como resultado {suma}')

    def restar(self):
        resta = self.entero1 - self.entero2
        print(f'La resta da como resultado {resta}')

    def dividir(self):
        division = self.entero1 // self.entero2
        print(f'La division de como resultado {division}')

    def multiplicar(self):
        multiplicacion = self.entero1 * self.entero2
        print(f'La multiplicacion da como resultado {multiplicacion}')
