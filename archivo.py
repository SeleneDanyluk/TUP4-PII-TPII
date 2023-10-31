from datetime import date


class Archivo:
    """
    Clase que describe los atributos y métodos necesarios de un archivo.

    Atributos:
        __nombre(str): Nombre del archivo.
        __formato(str): Formato del archivo.
        __fecha(date): Fecha del día de carga
    """
    def __init__(self, nombre: str, formato: str, fecha = date.today()) -> None:
        """
        La función __init__ iniciliza una referencia a la clase Profesor.

        Args:
            nombre(str): Nombre del archivo.
            formato(str): Formato del archivo.
            fecha(date): Fecha del día de carga
        """
        self.__nombre = nombre
        self.__formato = formato
        self.__fecha = fecha

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre

    @property
    def formato(self):
        return self.__formato

    @formato.setter
    def formato(self, nuevo_formato):
        self.__formato = nuevo_formato

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, nueva_fecha):
        self.__fecha = nueva_fecha

    def __str__(self) -> str:
        return f"{self.nombre}.{self.formato}"
