class Punto2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        texto = f'El objeto retorna " {self.x} "por un lado y " {self.y} "por otro'
        return texto
