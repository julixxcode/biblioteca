import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from datetime import date
from src.prestamo import Prestamo
from src.libro import Libro
from src.usuario import Usuario


# 🧪 TEST 1: Crear un préstamo correctamente
def test_crear_prestamo_correcto():
    libro = Libro("101", "Crónica de una muerte anunciada", "Gabriel García Márquez")
    usuario = Usuario(10, "Jair Orellano")
    prestamo = Prestamo(1, libro, usuario)
    assert prestamo.id == 1
    assert prestamo.libro.titulo == "Crónica de una muerte anunciada"
    assert prestamo.usuario.nombre == "Jair Orellano"
    assert prestamo.fecha_prestamo == date.today()
    assert prestamo.fecha_devolucion is None


# 🧪 TEST 2: Devolver un libro actualiza la fecha y disponibilidad
def test_devolver_libro_actualiza_estado():
    libro = Libro("102", "El Principito", "Antoine de Saint-Exupéry")
    usuario = Usuario(11, "Julian Murcia")
    usuario.agregar_libro(libro)
    libro.marcar_prestado()
    prestamo = Prestamo(2, libro, usuario)
    prestamo.devolver()
    assert prestamo.fecha_devolucion == date.today()
    assert libro.disponible is True
    assert libro not in usuario.libros_prestados


# 🧪 TEST 3: Fecha de préstamo se asigna automáticamente
def test_fecha_prestamo_por_defecto():
    libro = Libro("103", "1984", "George Orwell")
    usuario = Usuario(12, "Ana López")
    prestamo = Prestamo(3, libro, usuario)
    assert isinstance(prestamo.fecha_prestamo, date)


# 🧪 TEST 4: Fecha de devolución se puede establecer manualmente
def test_fecha_devolucion_manual():
    libro = Libro("104", "Fahrenheit 451", "Ray Bradbury")
    usuario = Usuario(13, "Carlos Pérez")
    fecha_manual = date(2024, 1, 10)
    prestamo = Prestamo(4, libro, usuario, fecha_prestamo=date(2024, 1, 1), fecha_devolucion=fecha_manual)
    assert prestamo.fecha_devolucion == fecha_manual


# 🧪 TEST 5: El método devolver cambia los estados correctamente solo una vez
def test_devolver_libro_solo_una_vez():
    libro = Libro("105", "El Hobbit", "J.R.R. Tolkien")
    usuario = Usuario(14, "Camila Torres")
    usuario.agregar_libro(libro)
    libro.marcar_prestado()
    prestamo = Prestamo(5, libro, usuario)
    prestamo.devolver()
    fecha_primera = prestamo.fecha_devolucion
    # Si lo intenta devolver otra vez, no debe cambiar la fecha ni lanzar error
    prestamo.devolver()
    assert prestamo.fecha_devolucion == fecha_primera
