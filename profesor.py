from usuario import Usuario
from curso import Curso


class Profesor(Usuario):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str, titulo: str, anio_egreso: int) -> None:
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
        self.mis_cursos.append(curso)
