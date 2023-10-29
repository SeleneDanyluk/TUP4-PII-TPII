from estudiante import Estudiante
from profesor import Profesor
from carrera import *
from curso import *
# from curso import Curso

estudiantes = [
    Estudiante("Jose", "Perez", "joseperez@gmail.com", "josesito1234", 54789, 2022), 
    Estudiante("Martin", "Rodriguez", "rodrimartin@gmail.com", "martinsito247", 50234, 2020),
    Estudiante("Martin", "Rodriguez", "mr@ejemplo.com", "martincho", 50234, 2020)
]

profesores = [
    Profesor("Jorge", "Ramirez", "jorgeramirez@hotmail.com", "jorgitoalfajor", "Profesorado de Matematicas", 1998), 
    Profesor("Maria", "Tomaseti", "mariatomaseti@hotmail.com", "maria4566", "Tecnica en Programación", 2010),
    Profesor("Jorge", "Ramirez", "jr@ejemplo.com", "jorge", "Profesorado de Matematicas", 1998)
]

cursos = [
    # Curso("Ingles I"),
    # Curso("Ingles II"),
    # Curso("Laboratorio I"),
    # Curso("Laboratorio II"),
    # Curso("Programacion I"),
    # Curso("Programacion II")
]

nueva_carrera = Carrera("Tecnicatura Universitaria en Programación", 2)

carreras = [
    nueva_carrera
]

nueva_carrera.materias.append(Curso("Ingles I"))
nueva_carrera.materias.append(Curso("Programacion I"))