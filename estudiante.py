from usuario import Usuario
from curso import Curso


class Estudiante(Usuario):
    """Clase que describe los atributos y métodos necesarios de un estudiante.

    Atributos:
        _nombre(str): Nombre del estudiante.
        _apellido(str): Apellido del estudiante.
        _email(str): Email del estudiante.
        _contrasenia(str): contrasenia del estudiante.
        __legajo(str): legajo del estudiante.
        __anio_inscripcion_carrera(int): anio en que el estudiante se inscribio a la carrera.
        __mis_cursos(list[Curso]): lista de cursos a los que asiste el estudiante.
    """
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, legajo: int, anio_inscripcion_carrera: int) -> None:
        """
        La función __init__ iniciliza una referencia a la clase Estudiante.

        Args:
            nombre(str): Nombre del estudiante.
            apellido(str): Apellido del estudiante.
            email(str): Email del estudiante.
            contrasenia(str): contrasenia del estudiante.
            legajo(str): legajo del estudiante.
            anio_inscripcion_carrera(int): anio en que el estudiante se inscribio a la carrera.
        """
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anio_inscripcion_carrera = anio_inscripcion_carrera
        self.__mis_cursos = []

    @property
    def legajo(self) -> int:
        return self.__legajo

    @legajo.setter
    def legajo(self, nuevo_legajo: int):
        self.__legajo = nuevo_legajo

    @property
    def anio_inscripcion_carrera(self) -> int:
        return self.__anio_inscripcion_carrera

    @anio_inscripcion_carrera.setter
    def anio_inscripcion_carrera(self, nuevo_anio_inscripcion: int):
        self.__anio_inscripcion_carrera = nuevo_anio_inscripcion

    @property
    def mis_cursos(self) -> list:
        return self.__mis_cursos

    def __str__(self) -> str:
        return f"El estudiante es: {self.nombre}"

    def matricular_en_curso(self, curso: Curso) -> None:
        """
        Agrega un nuevo curso a la lista de cursos del estudiante.

        Args:
            curso(Curso): nuevo curso al que asistirá el estudiante.
        """
        self.mis_cursos.append(curso)
