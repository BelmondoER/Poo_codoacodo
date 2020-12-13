class Pelicula:

    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print(f"Se ha creado la pelicula {self.titulo}")

    def __str__(self):
        return f'{self.titulo} ({self.lanzamiento})'


class Catalogo:
    peliculas = []

    def __init__(self, peliculas=None):
        if peliculas is None:
            peliculas = []
        self.peliculas = peliculas

    def agregar(self, pelis):
        self.peliculas.append(pelis)

    def mostrar(self):
        for pel in self.peliculas:
            print(pel, "ese")


peli = Pelicula("alien", 120, 1981)
cat = Catalogo([peli])
cat.mostrar()
cat.agregar(Pelicula("ghost", 140, 1987))
cat.mostrar()
