import random
import string


class Curso:
    """Clase que describe los atributos y métodos necesarios de un curso.

    Atributos:
       __nombre(str): nombre del curso.
       __contrasenia_matriculacion(str): constrasenia de matriculacion al curso.
    """
    def __init__(self, nombre: str) -> None:
        """
        La función __init__ iniciliza una referencia a la clase Curso.

        Args:
            nombre(str): Nombre del curso.
        """
        self.__nombre = nombre
        self.__contrasenia_matriculacion = self.__generar_contrasenia()

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre

    @property
    def contrasenia_matriculacion(self) -> str:
        return self.__contrasenia_matriculacion

    def __str__(self) -> str:
        return f"Materia: {self.nombre}"

    @classmethod
    def __generar_contrasenia(cls) -> str:
        """
        Genera una contrasenia de matriculación aleatoriamente.

        Returns:
            (str): contrasenia de matriculacion al curso.
        """
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(password) for i in range(7))
