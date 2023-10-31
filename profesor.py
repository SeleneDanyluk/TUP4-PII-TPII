from usuario import Usuario
from curso import Curso


class Profesor(Usuario):
    """
    Clase que describe los atributos y métodos necesarios de un profesor.

    Atributos:
        _nombre(str): Nombre del profesor.
        _apellido(str): Apellido del profesor.
        _email(str): Email del profesor.
        _contrasenia(str): contrasenia del profesor.
        __titulo(str): titulo del profesor.
        __anio_egreso(int): anio en que el profesor obtuvo su titulo.
        __mis_cursos(list[Curso]): lista de cursos dictados por el profesor.
    """
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo: str, anio_egreso: int) -> None:
        """
        La función __init__ iniciliza una referencia a la clase Profesor.

        Args:
            nombre(str): Nombre del profesor.
            apellido(str): Apellido del profesor.
            email(str): Email del profesor.
            contrasenia(str): contrasenia del profesor.
            titulo(str): titulo del profesor.
            anio_egreso(int): anio en que el profesor obtuvo su titulo.
        """
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anio_egreso = anio_egreso
        self.__mis_cursos = []

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo: str):
        self.__titulo = titulo

    @property
    def anio_egreso(self) -> int:
        return self.__anio_egreso

    @anio_egreso.setter
    def anio_egreso(self, anio_egreso: int):
        self.__anio_egreso = anio_egreso

    @property
    def mis_cursos(self) -> list:
        return self.__mis_cursos

    def __str__(self) -> str:
        return f"El profesor es: {self.nombre}"

    def dictar_curso(self, curso: Curso) -> None:
        """
        Agrega un nuevo curso a la lista de cursos dictados por el profesor.

        Args:
            curso(Curso): nuevo curso a dictar por el profesor.
        """
        self.mis_cursos.append(curso)
