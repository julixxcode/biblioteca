class Libro:
    def __init__(self, isbn, titulo, autor, disponible=True):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def marcar_prestado(self):
        if not self.disponible:
            raise ValueError("El libro ya está prestado")
        self.disponible = False

    def marcar_disponible(self):
        self.disponible = True
