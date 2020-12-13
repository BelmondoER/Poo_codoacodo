class AlumnoyNota:

    listaAlumnos = []
    listaNotas = []

    def elegir_opcion(self):
        opcion = 0
        while opcion != 4:
            print('---------Menu-----------')
            print('1----Cargar alumnos')
            print('2----Listar alumnos')
            print('3----Mostrar alumnos con notas mayores o iguales a 7')
            print('4----Salir del programa')
            opcion = int(input('Ingrese una opcion del menu'))

            if opcion == 1:
                self.cargar_alumnos()
            elif opcion == 2:
                self.listar_alumnos()
            elif opcion == 3:
                self.mostrar_aprobados()
        print(" Hasta luego ")

    def cargar_alumnos(self):
        self.alumno = input('Ingrese el nombre del alumno: ')
        self.listaAlumnos.append(self.alumno)
        self.nota = int(input('Ingrese la calificacion del alumno: '))
        self.listaNotas.append(self.nota)

    def listar_alumnos(self):
        print('------------Listando alumnos--------------------')
        for i in range(len(self.listaAlumnos)):
            print(f'{self.listaAlumnos[i]} tiene como nota {self.listaNotas[i]}')
        print('------------++++++++++++++++--------------------')
    def mostrar_aprobados(self):
        print('------------Alumnos aprobados--------------------')
        for i in range(len(self.listaAlumnos)):
            if self.listaNotas[i] >=7:
                print(f'{self.listaAlumnos[i]} tiene como nota {self.listaNotas[i]}')
        print('------------++++++++++++++++--------------------')