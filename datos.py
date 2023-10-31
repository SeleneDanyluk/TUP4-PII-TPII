from estudiante import Estudiante
from profesor import Profesor
from carrera import *
from curso import *
# from curso import Curso


profesores = [
    Profesor("Jorge", "Ramirez", "jorgeramirez@hotmail.com", "jorgitoalfajor", "Profesorado de Matematicas", 1998), 
    Profesor("Maria", "Tomaseti", "mariatomaseti@hotmail.com", "maria4566", "Tecnica en Programación", 2010),
    Profesor("Jorge", "Ramirez", "jr@ejemplo.com", "jorge", "Profesorado de Matematicas", 1998),
    Profesor("Jorge", "Ra", "c", "d", "Profesorado de Matematicas", 1998),
]


nueva_carrera = Carrera("Tecnicatura Universitaria en Programación", 2)

carreras = [
    nueva_carrera
]

estudiantes = [
    Estudiante("Jose", "Perez", "joseperez@gmail.com", "josesito1234", 54789, 2022, nueva_carrera), 
    Estudiante("Martin", "Rodriguez", "rodrimartin@gmail.com", "martinsito247", 50234, 2020, nueva_carrera),
    Estudiante("Martin", "Rodriguez", "mr@ejemplo.com", "martincho", 50234, 2020, nueva_carrera),
    Estudiante("Jose", "Lopez", "a", "b", 50321, 2020, nueva_carrera)
]