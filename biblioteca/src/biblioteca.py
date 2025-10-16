from src.libro import Libro
from src.usuario import Usuario
from src.prestamo import Prestamo

class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.usuarios = []
        self.prestamos = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_libro(self, titulo):
        return [l for l in self.catalogo if titulo.lower() in l.titulo.lower()]

    def prestar_libro(self, isbn, id_usuario):
        libro = next((l for l in self.catalogo if l.isbn == isbn), None)
        usuario = next((u for u in self.usuarios if u.id == id_usuario), None)
        if not libro:
            raise ValueError("Libro no encontrado")
        if not usuario:
            raise ValueError("Usuario no encontrado")
        if not libro.disponible:
            raise ValueError("Libro no disponible")

        libro.marcar_prestado()
        usuario.agregar_libro(libro)
        prestamo = Prestamo(len(self.prestamos)+1, libro, usuario)
        self.prestamos.append(prestamo)
        return prestamo

    def devolver_libro(self, isbn, id_usuario):
        prestamo = next(
            (p for p in self.prestamos if p.libro.isbn == isbn and p.usuario.id == id_usuario and not p.fecha_devolucion),
            None
        )
        if not prestamo:
            raise ValueError("No se encontró el préstamo activo")
        prestamo.devolver()
        return prestamo
