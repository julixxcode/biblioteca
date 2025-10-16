import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.biblioteca import Biblioteca
from src.libro import Libro
from src.usuario import Usuario
from src.prestamo import Prestamo


# 🧪 TEST 1: Crear una biblioteca vacía
def test_crear_biblioteca_vacia():
    b = Biblioteca()
    assert b.catalogo == []
    assert b.usuarios == []
    assert b.prestamos == []


# 🧪 TEST 2: Agregar un libro al catálogo
def test_agregar_libro():
    b = Biblioteca()
    libro = Libro("001", "1984", "George Orwell")
    b.agregar_libro(libro)
    assert len(b.catalogo) == 1
    assert b.catalogo[0].titulo == "1984"


# 🧪 TEST 3: Registrar un usuario
def test_registrar_usuario():
    b = Biblioteca()
    usuario = Usuario(1, "Jair Orellano")
    b.registrar_usuario(usuario)
    assert len(b.usuarios) == 1
    assert b.usuarios[0].nombre == "Jair Orellano"


# 🧪 TEST 4: Buscar libro por título
def test_buscar_libro_por_titulo():
    b = Biblioteca()
    libro1 = Libro("002", "El Principito", "Antoine de Saint-Exupéry")
    libro2 = Libro("003", "Cien años de soledad", "Gabriel García Márquez")
    b.agregar_libro(libro1)
    b.agregar_libro(libro2)
    resultados = b.buscar_libro("Cien")
    assert len(resultados) == 1
    assert resultados[0].autor == "Gabriel García Márquez"


# 🧪 TEST 5: Prestar un libro correctamente
def test_prestar_libro_exitosamente():
    b = Biblioteca()
    libro = Libro("004", "El Hobbit", "J.R.R. Tolkien")
    usuario = Usuario(2, "Laura Gómez")
    b.agregar_libro(libro)
    b.registrar_usuario(usuario)

    prestamo = b.prestar_libro("004", 2)
    assert isinstance(prestamo, Prestamo)
    assert prestamo.libro.disponible is False
    assert len(usuario.libros_prestados) == 1


# 🧪 TEST 6: No se puede prestar un libro no disponible
def test_error_prestar_libro_no_disponible():
    b = Biblioteca()
    libro = Libro("005", "Fahrenheit 451", "Ray Bradbury", disponible=False)
    usuario = Usuario(3, "Carlos Pérez")
    b.agregar_libro(libro)
    b.registrar_usuario(usuario)

    with pytest.raises(ValueError) as excinfo:
        b.prestar_libro("005", 3)
    assert "Libro no disponible" in str(excinfo.value)


# 🧪 TEST 7: No se puede prestar si el libro no existe
def test_error_libro_no_encontrado():
    b = Biblioteca()
    usuario = Usuario(4, "Ana López")
    b.registrar_usuario(usuario)
    with pytest.raises(ValueError) as excinfo:
        b.prestar_libro("999", 4)
    assert "Libro no encontrado" in str(excinfo.value)


# 🧪 TEST 8: No se puede prestar si el usuario no existe
def test_error_usuario_no_encontrado():
    b = Biblioteca()
    libro = Libro("006", "Crónica de una muerte anunciada", "Gabo")
    b.agregar_libro(libro)
    with pytest.raises(ValueError) as excinfo:
        b.prestar_libro("006", 999)
    assert "Usuario no encontrado" in str(excinfo.value)


# 🧪 TEST 9: Devolver un libro correctamente
def test_devolver_libro_correctamente():
    b = Biblioteca()
    libro = Libro("007", "La Odisea", "Homero")
    usuario = Usuario(5, "Julian Murcia")
    b.agregar_libro(libro)
    b.registrar_usuario(usuario)

    prestamo = b.prestar_libro("007", 5)
    assert not libro.disponible

    b.devolver_libro("007", 5)
    assert libro.disponible is True
    assert prestamo.fecha_devolucion is not None


# 🧪 TEST 10: Error al devolver un libro no prestado
def test_error_devolver_libro_no_prestado():
    b = Biblioteca()
    libro = Libro("008", "Ilíada", "Homero")
    usuario = Usuario(6, "Camila Torres")
    b.agregar_libro(libro)
    b.registrar_usuario(usuario)

    with pytest.raises(ValueError) as excinfo:
        b.devolver_libro("008", 6)
    assert "No se encontró el préstamo activo" in str(excinfo.value)
