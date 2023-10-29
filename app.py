import os
from datos import estudiantes, profesores, cursos, carreras
from profesor import Profesor
from curso import Curso
from typing import Union
from usuario import Usuario
from estudiante import Estudiante

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
    print("2. Ver curso.")
    print("3. Volver al menú principal")


def subMenu_profesor():
    print("1. Dictar curso.")
    print("2. Ver curso.")
    print("3. Volver al menú principal")

def registrar_profesor():
    nombre = input("Ingrese nombre")
    apellido = input("Ingrese apellido")
    email = input("Ingrese email")
    password = input("Ingrese contra")
    titulo = input("Ingrese titulo")
    anio_egreso = input("ingrese anio egreso")

    profesores.append(Profesor(nombre, apellido, email, password, titulo, anio_egreso))


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
    es_profesor = input("Si es profesor ingrese el dodigo admin para darse de alta, sino presione enter")
    if es_profesor.lower() == "admin":
        registrar_profesor()
    return False, usuario


def ver_curso(usuario: object, curso: Curso):
    """Muestra el nombre del curso si el usuario es alumno y nombre y contraseña si el usuario es Profesor :
     Args:
        Usuario: Objeto usuario (Profesor / Estudiante).

    Returns:
        None
    """
    print(f"Nombre: {curso.nombre}")
    if isinstance(usuario, Profesor):
        print(f"Contraseña: {curso.contrasenia_matriculacion}")


def listar_cursos(cursos: list, mensaje: str) -> Curso:
    """Muestra un listado de los cursos y solicita el ingreso del número correspondiente a uno de ellos:
     Args:
        Cursos: Lista de cursos.
        Mensaje: Para matricularse en un curso o para visualizarlo segun el usuario.
    Returns:
        Curso: Devuelve un curso en caso de que existan

        None: En caso de no existir cursos
    """
    cursos_disponibles = {}
    if len(cursos) != 0:
        for i, curso in enumerate(cursos, 1):
            cursos_disponibles[str(i)] = curso
            print(f"{i} {curso.nombre}")
        while True:
            opt_curso = input(mensaje)
            if not opt_curso.isnumeric() or int(opt_curso) < 1 or int(opt_curso) > len(cursos):
                print("La opción ingresada es inválida")
                continue
            break
        return cursos_disponibles[str(opt_curso)]
    else:
        return None


def mostrar_cursos(usuario: object):
    """Muestra un listado de los cursos en los que se encuentra el usuario y luego imprime la opcion deseada :
     Args:
        Usuario: Objeto usuario (Profesor / Estudiante).

    Returns:
        None
    """
    curso_seleccionado = listar_cursos(usuario.mis_cursos, "Ingrese la opción correspondiente para ver más información: ")
    if curso_seleccionado is not None:
        ver_curso(usuario, curso_seleccionado)
    else:
        print("No hay cursos cargados.")


def esta_matriculado(estudiante: Estudiante, curso: Curso) -> bool:
    for curso_estudiante in estudiante.mis_cursos:
        if curso_estudiante == curso:
            print("Usted ya se encuentra matriculado en este curso.")
            return True
    return False


def matricularse_curso(estudiante: Estudiante):
    """Llama a la función listar cursos y solicita el ingreso de una opción si hay cursos disponibles. Solicita la contraseña correspondiente y la valida:
     Args:
        Usuario: Objeto Estudiante.

    Returns:
        None
    """
    curso_seleccionado = listar_cursos(cursos, "Ingrese el curso que quiere matricularse: ")
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


def dictar_nuevo_curso(profesor: Profesor):
    """Solicita un nombre para el curso a dictar y lo agrega a la lista de cursos general y los que dicta el profesor. Llama a la función ver_curso para imprimir los datos:
     Args:
        Usuario: Objeto Profesor.

    Returns:
        None
    """
    nombre_curso = input("Ingrese el nombre del curso que desea dictar: ")
    # Ver si es numero
    curso = Curso(nombre_curso)
    cursos.append(curso)
    profesor.dictar_curso(curso)
    print("El curso ha sido ingresado correctamente !!!")
    ver_curso(profesor, curso)


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
    while respuesta != "salir":
        subMenu_alumno()
        opt_alumno = input("\n Ingrese la opción de menú: ")
        os.system("cls")
        if opt_alumno.isnumeric():
            if int(opt_alumno) == 1:
                matricularse_curso(estudiante)
            elif int(opt_alumno) == 2:
                mostrar_cursos(estudiante)
            elif int(opt_alumno) == 3:
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
    while respuesta != "salir":
        subMenu_profesor()
        opt_profesor = input("\nIngrese la opción de menú: ")
        os.system("cls")
        if opt_profesor.isnumeric():
            if int(opt_profesor) == 1:
                dictar_nuevo_curso(profesor)
            elif int(opt_profesor) == 2:
                mostrar_cursos(profesor)
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
