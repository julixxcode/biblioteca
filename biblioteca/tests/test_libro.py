import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from src.libro import Libro


# 🧪 TEST 1: Creación correcta de un libro
def test_crear_libro():
    libro = Libro("001", "1984", "George Orwell")
    assert libro.isbn == "001"
    assert libro.titulo == "1984"
    assert libro.autor == "George Orwell"
    assert libro.disponible is True


# 🧪 TEST 2: Marcar libro como prestado
def test_marcar_prestado():
    libro = Libro("002", "El principito", "Antoine de Saint-Exupéry")
    libro.marcar_prestado()
    assert libro.disponible is False


# 🧪 TEST 3: No se puede prestar un libro ya prestado
def test_error_si_libro_ya_prestado():
    libro = Libro("003", "Cien años de soledad", "Gabriel García Márquez", disponible=False)
    with pytest.raises(ValueError) as excinfo:
        libro.marcar_prestado()
    assert "El libro ya está prestado" in str(excinfo.value)


# 🧪 TEST 4: Marcar libro como disponible nuevamente
def test_marcar_disponible():
    libro = Libro("004", "Fahrenheit 451", "Ray Bradbury", disponible=False)
    libro.marcar_disponible()
    assert libro.disponible is True


# 🧪 TEST 5: Validar que el libro cambie de estado correctamente
def test_cambio_estado_de_prestamo_y_disponibilidad():
    libro = Libro("005", "El Hobbit", "J.R.R. Tolkien")
    assert libro.disponible is True  # inicialmente disponible
    libro.marcar_prestado()
    assert libro.disponible is False  # después de prestar
    libro.marcar_disponible()
    assert libro.disponible is True  # después de devolver
