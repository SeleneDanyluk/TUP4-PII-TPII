import random
import string
from archivo import *


class Curso:
    """Clase que describe los atributos y métodos necesarios de un curso.

    Atributos:
       __nombre(str): nombre del curso.
       __contrasenia_matriculacion(str): constrasenia de matriculacion al curso.
    """
    __prox_cod = int(0)

    def __init__(self, nombre: str) -> None:
        """
        La función __init__ iniciliza una referencia a la clase Curso.

        Args:
            nombre(str): Nombre del curso.
        """
        self.__nombre = nombre
        self.__contrasenia_matriculacion = self.__generar_contrasenia()
        self.__archivos = []

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre

    @property
    def contrasenia_matriculacion(self) -> str:
        return self.__contrasenia_matriculacion
    
    @property
    def archivos(self):
        return self.__archivos
    
    @archivos.setter
    def archivos(self, nuevo_archivo):
        self.__archivos = nuevo_archivo

    def __str__(self) -> str:
        return f"Materia: {self.nombre}"
    
    @property
    def codigo(cls):
        cls.__prox_cod = cls.__prox_cod + 1
        return cls.__prox_cod

    @classmethod
    def __generar_contrasenia(cls) -> str:
        """
        Genera una contrasenia de matriculación aleatoriamente.

        Returns:
            (str): contrasenia de matriculacion al curso.
        """
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits
        return ''.join(random.choice(password) for i in range(7))

    def nuevo_archivo(self, archivo: Archivo):
        self.archivos.append(archivo)