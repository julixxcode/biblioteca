import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.usuario import Usuario
from src.libro import Libro


# 🧪 TEST 1: Crear un usuario correctamente
def test_crear_usuario():
    usuario = Usuario(1, "Jair Orellano")
    assert usuario.id == 1
    assert usuario.nombre == "Jair Orellano"
    assert usuario.libros_prestados == []


# 🧪 TEST 2: Agregar un libro al usuario
def test_agregar_libro_al_usuario():
    usuario = Usuario(2, "Julian Murcia")
    libro = Libro("001", "El Principito", "Antoine de Saint-Exupéry")
    usuario.agregar_libro(libro)
    assert len(usuario.libros_prestados) == 1
    assert usuario.libros_prestados[0].titulo == "El Principito"


# 🧪 TEST 3: Devolver un libro correctamente
def test_devolver_libro_del_usuario():
    usuario = Usuario(3, "Camila Torres")
    libro = Libro("002", "Cien años de soledad", "Gabriel García Márquez")
    usuario.agregar_libro(libro)
    usuario.devolver_libro(libro)
    assert libro not in usuario.libros_prestados


# 🧪 TEST 4: Error al devolver un libro que no tiene
def test_error_devolver_libro_no_prestado():
    usuario = Usuario(4, "Carlos Pérez")
    libro = Libro("003", "1984", "George Orwell")
    with pytest.raises(ValueError):
        usuario.devolver_libro(libro)


# 🧪 TEST 5: Usuario puede tener múltiples libros prestados
def test_usuario_con_varios_libros():
    usuario = Usuario(5, "Laura Gómez")
    libro1 = Libro("004", "El Hobbit", "J.R.R. Tolkien")
    libro2 = Libro("005", "Fahrenheit 451", "Ray Bradbury")
    usuario.agregar_libro(libro1)
    usuario.agregar_libro(libro2)
    assert len(usuario.libros_prestados) == 2
    titulos = [libro.titulo for libro in usuario.libros_prestados]
    assert "El Hobbit" in titulos
    assert "Fahrenheit 451" in titulos
