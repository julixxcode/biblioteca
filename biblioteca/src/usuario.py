class Usuario:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.libros_prestados = []

    def agregar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)
