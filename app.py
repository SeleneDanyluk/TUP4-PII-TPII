import os
from datos import estudiantes, profesores, cursos
from profesor import Profesor
from curso import Curso

#-----------------------------------------------Funciones------------------------------------------------------


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


def ingreso_credenciales(usuarios):
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
    print("El email ingresado no se encuentra registrado, debe registrarse")
    return False, usuario


def ver_curso(usuario, curso):
    print(f"Nombre: {curso.nombre}")
    if isinstance(usuario, Profesor):
        print(f"Contraseña: {curso.contrasenia_matriculacion}")


def listar_cursos(cursos, mensaje):
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


def matricularse_curso(estudiante):
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


def esta_matriculado(estudiante, curso) -> bool:
    for curso_estudiante in estudiante.mis_cursos:
        if curso_estudiante == curso:
            print("Usted ya se encuentra matriculado en este curso.")
            return True
    return False


def dictar_nuevo_curso(profesor):
    nombre_curso = input("Ingrese el nombre del curso que desea dictar: ")
    # Ver si es numero
    curso = Curso(nombre_curso)
    cursos.append(curso)
    profesor.dictar_curso(curso)
    print("El curso ha sido ingresado correctamente !!!")
    ver_curso(profesor, curso)


def mostrar_cursos(usuario):
    curso_seleccionado = listar_cursos(usuario.mis_cursos, "Ingrese el curso que quiere visualizar: ")
    if curso_seleccionado is not None:
        ver_curso(usuario, curso_seleccionado)
    else:
        print("No hay cursos cargados.")


def ver_cursos_alfabeticamente():
    if len(cursos)>= 1:
        cursos_ordenados = sorted(cursos, key=lambda curso: curso.nombre)
        for curso in cursos_ordenados:
            print(f"{curso} - Carrera: Tecnicatura Universitaria en Programación")
    else:
        print("Aun no hay cursos disponibles")

#  -----------------------------------------------Alumno------------------------------------------------------


def ingreso_alumno(estudiante):
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


def ingreso_profesor(profesor):
    respuesta = ''
    while respuesta != "salir":
        subMenu_profesor()
        opt_profesor = input("\n Ingrese la opción de menú: ")
        os.system ("cls")
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













