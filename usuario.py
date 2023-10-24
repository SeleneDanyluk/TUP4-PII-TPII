from abc import ABC, abstractmethod


class Usuario(ABC):
    """
    Clase abstracta que describe los atributos y métodos necesarios de un usuario.

    Atributos:
        _nombre(str): Nombre del usuario.
        _apellido(str): Apellido del usuario.
        _email(str): Email del usuario.
        _contrasenia(str): contrasenia del usuario.
    """
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str) -> None:
        """
        La función __init__ iniciliza una referencia a la clase Usuario.

        Args:
            nombre(str): Nombre del usuario.
            apellido(str): Apellido del usuario.
            email(str): Email del usuario.
            contrasenia(str): contrasenia del usuario.
        """
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, nuevo_apellido: str):
        self._apellido = nuevo_apellido

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, nuevo_email: str):
        self._email = nuevo_email

    @property
    def contrasenia(self) -> str:
        return self._contrasenia

    @contrasenia.setter
    def contrasenia(self, nueva_contrasenia: str):
        self._contrasenia = nueva_contrasenia

    def validar_credenciales(self, email_ingresado: str, contrasenia_ingresada: str) -> bool:
        """
        Valida que las credenciales dadas sean las correctas.

        Args:
            email_ingresado(str): email ingresado.
            contrasenia_ingresada(str): contrasenia ingresada.

        Returns:
            (bool): True si las credenciales dadas son correctas, False en caso contrario.
        """
        return self.email == email_ingresado and self.contrasenia == contrasenia_ingresada

    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError
