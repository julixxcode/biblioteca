from datetime import date

class Prestamo:
    def __init__(self, id, libro, usuario, fecha_prestamo=None, fecha_devolucion=None):
        self.id = id
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo or date.today()
        self.fecha_devolucion = fecha_devolucion

    def devolver(self):
        # Si ya fue devuelto, no hacer nada
        if self.fecha_devolucion:
            return
        
        self.fecha_devolucion = date.today()
        
        # Solo intentar devolver si el libro sigue en la lista del usuario
        if self.libro in self.usuario.libros_prestados:
            self.usuario.devolver_libro(self.libro)
        
        self.libro.marcar_disponible()
