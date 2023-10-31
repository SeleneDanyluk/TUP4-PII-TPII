import os
from datos import estudiantes, profesores, carreras
from profesor import Profesor
from curso import Curso
from typing import Union
from usuario import Usuario
from estudiante import Estudiante
from archivo import Archivo

#  -----------------------------------------------Funciones------------------------------------------------------


def mensaje_bienvenida():
    print("Bienvenido/a al campus virtual!")


def menu_principal():
    print("1 - Ingresar como alumno.")
    print("2 - Ingresar como profesor.")
    print("3 - Ver cursos.")
    print("4 - Salir.")


def subMenu_alumno():
    print("1. Matricularse a un curso.")
    print("2. Desmatricularse de un curso.")
    print("3. Ver cursos.")
    print("4. Volver al menú principal")


def subMenu_profesor():
    print("1. Dictar curso.")
    print("2. Ver curso.")
    print("3. Volver al menú principal")


def ingreso_credenciales(usuarios: list) -> Union[bool, Usuario]:
    """Valida el ingreso de email y luego de la contraseña:
     Args:
        Usuarios(list[Usuario]): Lista de usuarios registrados.

    Returns:
        Union[True, Usuario]: Las credenciales ingresadas son validas.
        Union[False, Usuario]: La contraseña ingresada es incorrecta, muestra mensaje de error.
    """
    email = input("Ingrese su email: ")
    for usuario in usuarios:
        if usuario.email == email:
            password = input("Ingrese su contraseña: ")
            if usuario.validar_credenciales(email, password):
                print("Usted ingreso correctamente al sistema")
                return True, usuario
            else:
                print("La contraseña ingresada es incorrecta")
                return False, usuario
    print("El email ingresado no se encuentra registrado, debe registrarse") #si es profesor ingrese el codigo admin y que llame a la funcion dar de alta prof
    es_profesor = input("Si es profesor ingrese el código admin para darse de alta, de lo contrario presione enter: ")
    if es_profesor.lower() == "admin":
        registrar_profesor()
    return False, usuario

def ver_archivos(curso: Curso):
    """Muestra los archivos del curso seleccionado de existir alguno :
        Args:
         curso(Curso): objeto curso.
        Returns:
         None
    """
    if len(curso.archivos) != 0:
        print("Archivos de la materia: ")
        for archivo in sorted(curso.archivos, key=lambda archivo: archivo.fecha):
            print(archivo)

def registrar_profesor():
    """Solicita el ingreso de datos del profesor y agrega el objeto a la lista de profesores :

    Returns:
        None
    """
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    email = input("Ingrese su email: ")
    password = input("Ingrese una contraseña: ")
    titulo = input("Ingrese su título: ")
    anio_egreso = input("ingrese el año de egreso: ")

    profesores.append(Profesor(nombre, apellido, email, password, titulo, anio_egreso))

    print("Se ha registrado correctamente.")


def ver_curso(usuario: object, curso: Curso, identificador: int):
    """Muestra el nombre del curso si el usuario es alumno y nombre y contraseña si el usuario es Profesor :
     Args:
        usuario(Usuario): Objeto usuario (Profesor / Estudiante).
        curso(Curso): objeto curso.
        indentificador(int): numero que identifica el tipo de usuario 1 alumno, 2 profesor

    Returns:s
        None
    """
    if identificador == 1:
        print(f"Materia: {curso.nombre}")
        ver_archivos(curso)
    else:
        print(f"Nombre: {curso.nombre}")
        print(f"Codigo: {curso.codigo}")
        print(f"Contraseña: {curso.contrasenia_matriculacion}")
        if identificador == 2:
            print(f"Cantidad de archivos: {len(curso.archivos)} ")




def listar_cursos(lista: list, mensaje: str) -> Curso: # Modificar esta funcion
    """Muestra un listado de los cursos y solicita el ingreso del número correspondiente a uno de ellos:
     Args:
        Cursos: Lista de cursos.
        Mensaje: Para matricularse en un curso o para visualizarlo segun el usuario.
    Returns:
        Curso: Devuelve un curso en caso de que existan

        None: En caso de no existir cursos
    """
    lista_disponibles = {}
    if len(lista) != 0:
        for i, item in enumerate(lista, 1):
            lista_disponibles[str(i)] = item
            print(f"{i} {item.nombre}")
        while True:
            opt_item = input(mensaje)
            if not opt_item.isnumeric() or int(opt_item) < 1 or int(opt_item) > len(lista):
                print("La opción ingresada es inválida")
                continue
            break
        return lista_disponibles[str(opt_item)]
    else:
        return None


def mostrar_cursos(usuario: object, identificador: int):
    """Muestra un listado de los cursos en los que se encuentra el usuario y luego imprime la opcion deseada :
     Args:
        Usuario: Objeto usuario (Profesor / Estudiante).

    Returns:
        None
    """
    curso_seleccionado = listar_cursos(usuario.mis_cursos, "Ingrese la opción correspondiente para ver más información: ")
    if curso_seleccionado is not None:
        ver_curso(usuario, curso_seleccionado, identificador)
        if isinstance(usuario, Profesor):
            desea_cargar = input("Desea cargar un archivo? S/N: ")
            if desea_cargar.upper() == "S":
                agregar_archivo(curso_seleccionado)
    else:
        print("No hay cursos cargados.")


def esta_matriculado(estudiante: Estudiante, curso: Curso) -> bool:
    """Evalua si el estudiante esta matriculado en el curso:
        Args: 
            estudiante(Estudiante): Objeto estudiante.
            curso(Curso): objeto curso.

    Returns:
        True: si el estudiante se encuentra matriculado.
        False: en caso de no estar matriculado en el curso.
    """
    for curso_estudiante in estudiante.mis_cursos:
        if curso_estudiante == curso:
            print("Usted ya se encuentra matriculado en este curso.")
            return True
    return False


def matricularse_curso(estudiante: Estudiante):
    """Llama a la función listar cursos y solicita el ingreso de una opción si hay cursos disponibles. Solicita la contraseña correspondiente y la valida:
     Args:
        estudiante(Estudiante): Objeto Estudiante.

    Returns:
        None
    """
    curso_seleccionado = listar_cursos(estudiante.carrera.materias, "Ingrese el curso que quiere matricularse: ")
    if curso_seleccionado is not None:
        if esta_matriculado(estudiante, curso_seleccionado):
            return
        contrasenia_ingresada = input("Ingrese la contraseña de matriculación: ")
        if contrasenia_ingresada == curso_seleccionado.contrasenia_matriculacion:
            estudiante.matricular_en_curso(curso_seleccionado)
            print(f"Usted se ha matriculado exitosamente!!: {curso_seleccionado.nombre}")
        else:
            print("La contraseña de matriculación ingresada es incorrecta.")
    else:
        print("No hay cursos cargados.")

def desmatricular_curso(estudiante: Estudiante):
    """Lista los cursos llamando a la funcion listar_cursos que devuelve el curso a desmatricularse. De ser asi lo elimina:
     Args:
        estudiante(Estudiante): Objeto Estudiante.

    Returns:
        None
    """
    curso_seleccionado = listar_cursos(estudiante.mis_cursos, "Ingrese el curso del cual desea desmatricularse: ")
    if curso_seleccionado is not None:
        estudiante.desmatricular_curso(curso_seleccionado)
        print("Usted se desmatriculo exitosamente.")
    else:
        print("Usted no posee matriculaciones activas.")

def agregar_archivo(curso: Curso):
    """Solicita los datos del archivo y agrega el objeto archivo a la lista de archivos del curso seleccionado:
     Args:
        curso(Curso): Objeto curso al que desea agregar el archivo.

    Returns:
        None
    """
    while True:
        nombre = input("Ingrese el nombre del archivo: ")
        formato = input("Ingrese el formato del archivo: ")
        nuevo_archivo = Archivo(nombre, formato)
        curso.nuevo_archivo(nuevo_archivo)
        print(f"Se agrego el archivo: {nuevo_archivo}")
        opt_archivo = input("Desea agregar otro archivo?(S/N)")
        if opt_archivo.upper() == "N":
            return


def dictar_nuevo_curso(profesor: Profesor, identificador: int):
    """Solicita un nombre para el curso a dictar y lo agrega a la lista de cursos general y los que dicta el profesor. Llama a la función ver_curso para imprimir los datos:
     Args:
        Usuario: Objeto Profesor.

    Returns:
        None
    """
    nombre_curso = input("Ingrese el nombre del curso que desea dictar: ")
    curso = Curso(nombre_curso)
    carrera_seleccionada = listar_cursos(carreras, "Ingrese la carrera en la cual quiere dictar el curso: ")
    carrera_seleccionada.materias.append(curso)
    profesor.dictar_curso(curso)
    print("El curso ha sido ingresado correctamente.")
    ver_curso(profesor, curso, identificador)


def ver_cursos_alfabeticamente():
    """Verifica que existan cursos y los imprime por orden alfabeticamente:

    Returns:
        None
    """
    carreras_ordenadas = sorted(carreras, key=lambda carrera: carrera.nombre)
    for carrera in carreras_ordenadas:
        materias_ordenadas = sorted(carrera.materias, key=lambda materia: materia.nombre)
        for materia in materias_ordenadas:
            print(f"{materia} - {carrera}")

#  -----------------------------------------------Alumno------------------------------------------------------


def ingreso_alumno(estudiante: Estudiante):
    """Muestra el submenu del alumno y solicita el ingreso de una opción para operar dentro del campo:
     Args:
        Usuario: Objeto Estudiante.

    Returns:
        None
    """
    respuesta = ''
    indentificador_alumno = 1
    while respuesta != "salir":
        subMenu_alumno()
        opt_alumno = input("\n Ingrese la opción de menú: ")
        os.system("cls")
        if opt_alumno.isnumeric():
            if int(opt_alumno) == 1:
                matricularse_curso(estudiante)
            elif int(opt_alumno) == 2:
                desmatricular_curso(estudiante)
            elif int(opt_alumno) == 3:
                mostrar_cursos(estudiante, indentificador_alumno)
            elif int(opt_alumno) == 4:
                respuesta = "salir"
            else:
                print("Ingrese una opción válida.")
        else:
            print("Ingrese una opción numérica.")


#  -----------------------------------------------Profesor------------------------------------------------------


def ingreso_profesor(profesor: Profesor):
    """Muestra el submenu del profesor y solicita el ingreso de una opción para operar dentro del campo:
     Args:
        Usuario: Objeto Profesor.

    Returns:
        None
    """
    respuesta = ''
    indentificador_profesor = 2
    while respuesta != "salir":
        subMenu_profesor()
        opt_profesor = input("\nIngrese la opción de menú: ")
        os.system("cls")
        if opt_profesor.isnumeric():
            if int(opt_profesor) == 1:
                dictar_nuevo_curso(profesor, indentificador_profesor)
            elif int(opt_profesor) == 2:
                mostrar_cursos(profesor, indentificador_profesor)
            elif int(opt_profesor) == 3:
                respuesta = "salir"
            else:
                print("Ingrese una opción válida.")
        else: 
            print("Ingrese una opción numérica.")


#  -----------------------------------------------App principal--------------------------------------------------


mensaje_bienvenida()
respuesta = ''

while respuesta != "salir":
    menu_principal()
    opt = input("\n Ingrese la opción de menú: ")
    os.system("cls")  # Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            validacion, estudiante = ingreso_credenciales(estudiantes)
            if validacion:
                ingreso_alumno(estudiante)
        elif int(opt) == 2:
            validacion, profesor = ingreso_credenciales(profesores)
            if validacion:
                ingreso_profesor(profesor)
        elif int(opt) == 3:
            ver_cursos_alfabeticamente()
        elif int(opt) == 4:
            respuesta = "salir"
        else:
            print("Ingrese una opción válida.")
    else:
        print("Ingrese una opción numérica.")

    input("Presione cualquier tecla para continuar....")  # Pausa

print("Hasta luego!.")
