import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from datetime import date
from src.biblioteca import Biblioteca
from src.libro import Libro
from src.usuario import Usuario


# 🧪 TEST 1: Flujo completo de préstamo y devolución con varios usuarios
def test_flujo_completo_biblioteca():
    b = Biblioteca()
    # Crear libros y usuarios
    libro1 = Libro("101", "1984", "George Orwell")
    libro2 = Libro("102", "El Principito", "Antoine de Saint-Exupéry")
    usuario1 = Usuario(1, "Jair Orellano")
    usuario2 = Usuario(2, "Julian Murcia")

    # Registrar en la biblioteca
    b.agregar_libro(libro1)
    b.agregar_libro(libro2)
    b.registrar_usuario(usuario1)
    b.registrar_usuario(usuario2)

    # Jair pide el libro 1
    prestamo1 = b.prestar_libro("101", 1)
    assert not libro1.disponible
    assert prestamo1.usuario == usuario1
    assert prestamo1.libro == libro1

    # Julian pide el libro 2
    prestamo2 = b.prestar_libro("102", 2)
    assert not libro2.disponible
    assert prestamo2.usuario == usuario2

    # Jair devuelve su libro
    b.devolver_libro("101", 1)
    assert libro1.disponible
    assert prestamo1.fecha_devolucion == date.today()

    # Julian aún no lo devuelve
    assert prestamo2.fecha_devolucion is None


# 🧪 TEST 2: Flujo con varios préstamos secuenciales del mismo libro
def test_prestamos_secuenciales_mismo_libro():
    b = Biblioteca()
    libro = Libro("201", "Cien años de soledad", "Gabriel García Márquez")
    usuario1 = Usuario(10, "Camila Torres")
    usuario2 = Usuario(11, "Laura Gómez")

    b.agregar_libro(libro)
    b.registrar_usuario(usuario1)
    b.registrar_usuario(usuario2)

    # Primer préstamo (Camila)
    prestamo1 = b.prestar_libro("201", 10)
    b.devolver_libro("201", 10)

    # Segundo préstamo (Laura)
    prestamo2 = b.prestar_libro("201", 11)
    b.devolver_libro("201", 11)

    assert prestamo1.fecha_devolucion is not None
    assert prestamo2.fecha_devolucion is not None
    assert libro.disponible is True


# 🧪 TEST 3: Intentar prestar y devolver varios libros a la vez
def test_prestamos_y_devoluciones_multiples():
    b = Biblioteca()
    libros = [
        Libro("301", "El Hobbit", "J.R.R. Tolkien"),
        Libro("302", "Fahrenheit 451", "Ray Bradbury"),
        Libro("303", "Crónica de una muerte anunciada", "Gabo")
    ]
    usuario = Usuario(20, "Daniel Martínez")

    for libro in libros:
        b.agregar_libro(libro)
    b.registrar_usuario(usuario)

    # Prestar todos los libros
    for l in libros:
        b.prestar_libro(l.isbn, usuario.id)

    assert all(not l.disponible for l in libros)
    assert len(usuario.libros_prestados) == 3

    # Devolver todos
    for l in libros:
        b.devolver_libro(l.isbn, usuario.id)

    assert all(l.disponible for l in libros)
    assert len(usuario.libros_prestados) == 0


# 🧪 TEST 4: Error al devolver libro de otro usuario
def test_error_devolver_libro_de_otro_usuario():
    b = Biblioteca()
    libro = Libro("401", "Don Quijote de la Mancha", "Miguel de Cervantes")
    usuario1 = Usuario(30, "Jair Orellano")
    usuario2 = Usuario(31, "Julian Murcia")

    b.agregar_libro(libro)
    b.registrar_usuario(usuario1)
    b.registrar_usuario(usuario2)

    b.prestar_libro("401", 30)

    with pytest.raises(ValueError) as excinfo:
        b.devolver_libro("401", 31)

    assert "No se encontró el préstamo activo" in str(excinfo.value)
