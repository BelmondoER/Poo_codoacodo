class Familia:

    def __init__(self, padre, madre, hijos=None):
        if hijos is None:
            hijos = []
        self.padre = padre
        self.madre = madre
        self.hijos = hijos

    def __str__(self):
        estring = f"La familia esta compuesta por:\nPapa : {self.padre} \n"
        estring += f"Mama : {self.madre} \n"
        if len(self.hijos):
            for hijo in self.hijos:
                estring += f'Hijo : {hijo} \n'
        return estring
