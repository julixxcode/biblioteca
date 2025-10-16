# 📚 Sistema de Gestión de Biblioteca

Proyecto académico desarrollado en Python para la gestión básica de una biblioteca.  
Permite **registrar libros, usuarios, realizar préstamos y devoluciones**, así como realizar **búsquedas por título**.  
El sistema fue creado aplicando principios de **Programación Orientada a Objetos (POO)** y **Testing Automatizado con Pytest**.

---

## 👨‍💻 Autor
**Julian Murcia**  
Desarrollador y estudiante de Ingeniería de Software  
_Fundación de Estudios Superiores Comfanorte (FESC), 2025_

---

## 🧱 Estructura del Proyecto

biblioteca/
│
├── src/ # Código fuente principal
│ ├── init.py
│ ├── biblioteca.py # Clase Biblioteca (gestiona libros, usuarios y préstamos)
│ ├── libro.py # Clase Libro
│ ├── usuario.py # Clase Usuario
│ └── prestamo.py # Clase Prestamo
│
├── tests/ # Suite de pruebas unitarias (Pytest)
│ ├── test_libro.py
│ ├── test_usuario.py
│ ├── test_prestamo.py
│ ├── test_biblioteca.py
│ └── test_integracion.py
│
├── htmlcov/ # Reporte HTML de cobertura
├── .venv/ # Entorno virtual (recomendado)
└── README.md # Documentación del proyecto

yaml
Copiar código

---

## ⚙️ Requisitos Previos

- **Python 3.10 o superior**
- **pip** (gestor de paquetes)
- Recomendado: crear un entorno virtual (`venv`)

---

## 🧩 Instalación

1. Clonar el repositorio o descargar el proyecto:
   ```bash
   git clone https://github.com/usuario/biblioteca.git
   cd biblioteca
Crear y activar entorno virtual:

bash
Copiar código
python -m venv .venv
.venv\Scripts\activate
Instalar dependencias:

bash
Copiar código
pip install pytest pytest-cov
🧪 Ejecución de Pruebas
Ejecutar todas las pruebas unitarias con cobertura:

bash
Copiar código
pytest tests/ -v --cov=src --cov-report=html
Esto generará un reporte visual de cobertura dentro de la carpeta:

bash
Copiar código
htmlcov/index.html
Abrir el reporte en el navegador:

bash
Copiar código
start htmlcov/index.html
📊 Resultados Esperados
Total de pruebas: 29

Cobertura esperada: ≥ 90 %

Todas las pruebas deben mostrar el estado:

nginx
Copiar código
PASSED ✅
Ejemplo de salida:

yaml
Copiar código
============================= 29 passed in 1.23s =============================
----------- coverage: platform win32, python 3.12.5-final-0 -----------
Coverage: 90%
HTML report generated: htmlcov/index.html
🧠 Descripción Técnica
Clase	Archivo	Responsabilidad
Libro	libro.py	Representa un libro del catálogo. Controla disponibilidad y estado de préstamo.
Usuario	usuario.py	Representa un lector registrado. Gestiona los libros prestados.
Prestamo	prestamo.py	Gestiona préstamos activos y fechas de devolución.
Biblioteca	biblioteca.py	Coordina libros, usuarios y préstamos. Controla errores y operaciones globales.

🧰 Tecnologías Utilizadas
Python 3.12

Pytest → pruebas unitarias

pytest-cov → análisis de cobertura

POO (Programación Orientada a Objetos)

HTML Report → reporte visual de cobertura

🏫 Valor Académico
Este proyecto representa una aplicación práctica del paradigma orientado a objetos y las buenas prácticas de pruebas de software (QA), alineado con las competencias de Codificación y Pruebas de Software en la FESC.

Se evaluaron los siguientes aspectos:

Diseño modular y reutilizable.

Correcta gestión de errores y excepciones.

Cobertura de código superior al 80 %.

Documentación técnica completa.

🏁 Créditos
Desarrollado por Julian Murcia
