class ListadoDeBebidas:

    def __init__(self):
        self.__bebida = "naranja"
        self.__bebidas_validas = ['naranja', 'manzana']

    @property
    def perr(self):
        return f"la bebida oficial es: {self.__bebida}"

    @perr.setter
    def bebidad(self, bebidad):
        self.__bebida = bebidad

bebidas = ListadoDeBebidas()
print(bebidas.perr)
bebidas.bebidad= "limonada"
print(bebidas.perr)
