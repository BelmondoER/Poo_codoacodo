class Alumno:
    nombre = ""
    nota = 0

    def inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_dato(self):
        print(f'Alumno : {self.nombre} Nota : {self.nota}')

    def mostrar_estado(self):
        if self.nota >= 4:
            print("Regular")
        else:
            print("Libre")