class Punto():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir_cuadrante(self):
        if self.x > 0 and self.y > 0:
            print('Cuadrante 1')
        elif self.x < 0 and self.y > 0:
            print('Cuadrante 2')
        elif self.x < 0 and self.y < 0:
            print('Cuadrante 3')
        elif self.x > 0 and self.y < 0:
            print('Cuadrante 4')
        else:
            print('Estas en el centro')

