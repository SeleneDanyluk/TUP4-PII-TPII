from estudiante import Estudiante
from profesor import Profesor
from curso import Curso

estudiantes = [
    Estudiante("Jose", "Perez", "joseperez@gmail.com", "josesito1234", 54789, 2022), 
    Estudiante("Martin", "Rodriguez", "rodrimartin@gmail.com", "martinsito247", 50234, 2020),
    Estudiante("Martin", "Rodriguez", "c", "d", 50234, 2020)
]

profesores = [
    Profesor("Jorge", "Ramirez", "jorgeramirez@hotmail.com", "jorgitoalfajor", "Profesorado de Matematicas", 1998), 
    Profesor("Maria", "Tomaseti", "mariatomaseti@hotmail.com", "maria4566", "Tecnica en Programación", 2010),
    Profesor("Jorge", "Ramirez", "a", "b", "Profesorado de Matematicas", 1998)
]

cursos = [
    Curso("Ingles I"),
    Curso("Ingles II"),
    Curso("Laboratorio I"),
    Curso("Laboratorio II"),
    Curso("Programacion I"),
    Curso("Programacion II")
]
