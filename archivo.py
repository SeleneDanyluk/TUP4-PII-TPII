from datetime import date

class Archivo:
    def __init__(self, nombre: str, formato: str, fecha = date.today()) -> None:
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