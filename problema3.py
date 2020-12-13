class Empleado:

    def __init__(self):
        self.nombre = input('Ingrese su nombre: ')
        self.sueldo = int(input('Ingrese su sueldo: '))

    def imprimir_datos(self):
        print(f'Nombre : {self.nombre} Sueldo : {self.sueldo}')

    def pagar_impuestos(self):
        if self.sueldo >30000:
            print('Pagara impuestos')
        else:
            print('No debe pagar impuestos')
