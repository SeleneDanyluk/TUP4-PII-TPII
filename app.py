import os
from datos import *
from usuario import Usuario
from estudiante import Estudiante
from profesor import Profesor

#-------------------------------------------------Datos--------------------------------------------------------
cursos_disponibles = ['crear listado de cursos disponibles para mostrar al usuario']

#ver si se hace una unica lista de usuarios o una para prof y otra para alumnos  


#-----------------------------------------------funciones------------------------------------------------------

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
    password = input("Ingrese su contraseña: ")
    for usuario in usuarios:
        if usuario.email == email:
            if usuario.validar_credenciales(email, password):
                return "Usted ingreso correctamente al sistema", True, usuario
            else:
                return "La contraseña ingresada es incorrecta", False, usuario
    return "El email ingresado no se encuentra registra, debe registrarse", False, usuario

def ver_curso(usuario, curso):
    if isinstance(usuario, Estudiante):
        for curso_usuario in usuario.mis_cursos:
            if curso == curso_usuario:
                print(f"Nombre: {curso.nombre}")
                break
    else:
        for curso_usuario in usuario.mis_cursos:
            if curso == curso_usuario:
                print(f"Nombre: {curso.nombre}")
                print(f"Contraseña: {curso.contrasenia_matriculacion}")
                break

def ingreso_alumno(estudiante):
    cursos_disponibles = {}
    respuesta = ''
    while respuesta != "salir":
        subMenu_alumno()
        opt_alumno = input("\n Ingrese la opción de menú: ")
        os.system ("cls")
        if opt_alumno.isnumeric():
            if int(opt_alumno) == 1:
                for i, curso in enumerate(cursos, 1):
                    cursos_disponibles[str(i)] = curso
                    print(f"{i} {curso.nombre}")
                opt_curso = input("Ingrese el curso que quiere matricularse: ")
                curso_seleccionado = cursos_disponibles[str(i)]
                for curso_estudiante in estudiante.mis_cursos:
                    if curso_estudiante == curso_seleccionado:
                        print("Usted ya se encuentra matriculado en este curso.")
                        continue
                contrasenia_ingresada = input("Ingrese la contraseña de matriculación: ")
                if contrasenia_ingresada == curso_seleccionado.contrasenia_matriculacion:
                    print(f"Usted ya es encuentra matriculado a la materia: {curso_seleccionado.nombre}")
                    estudiante.matricular_en_curso(curso_seleccionado)
                else:
                    print("La contraseña de matriculación ingresada es incorrecta.")
                    continue
                # if 1 < opt_curso > len(opt_curso):
                #     print("No es valido")
            elif int(opt_alumno) == 2:
                for i, curso in enumerate(estudiante.mis_cursos, 1):
                    cursos_disponibles[str(i)] = curso
                    print(f"{i} {curso.nombre}")
                opt_curso = input("Ingrese el curso que quiere visualizar: ")
                curso_seleccionado = cursos_disponibles[str(opt_curso)]
                ver_curso(estudiante, curso_seleccionado)
            elif int(opt_alumno) == 3:
                respuesta = "salir"
            else: 
                print("Ingrese una opción válida.")
        else: 
            print("Ingrese una opción numérica.")

def ingreso_profesor(profesor):
    cursos_disponibles = {}
    respuesta = ''
    while respuesta != "salir":
        subMenu_profesor()
        opt_profesor = input("\n Ingrese la opción de menú: ")
        os.system ("cls")
        if opt_profesor.isnumeric():
            if int(opt_profesor) == 1:
                nombre_curso = input("Ingrese el nombre del curso que desea dictar: ")
                # Ver si es numero
                curso = Curso(nombre_curso)
                cursos.append(curso)
                profesor.dictar_curso(curso)
                print("El curso ha sido ingresado correctamente !!!")
                ver_curso(profesor, curso)
            elif int(opt_profesor) == 2:
                for i, curso in enumerate(profesor.mis_cursos, 1):
                    cursos_disponibles[str(i)] = curso
                    print(f"{i} {curso.nombre}")
                opt_curso = input("Ingrese el curso que quiere visualizar: ")
                curso_seleccionado = cursos_disponibles[str(opt_curso)]
                ver_curso(profesor, curso_seleccionado)
            elif int(opt_profesor) == 3:
                respuesta = "salir"
            else: 
                print("Ingrese una opción válida.")
        else: 
            print("Ingrese una opción numérica.")

#-----------------------------------------------App principal----------------------------------------------------
mensaje_bienvenida()
respuesta = ''

while respuesta != "salir":
    menu_principal()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            mensaje, validacion, estudiante = ingreso_credenciales(estudiantes)
            if validacion:
                print(mensaje)
            else:
                print(mensaje)
                continue
            ingreso_alumno(estudiante)
        elif int(opt) == 2:
            mensaje, validacion, profesor = ingreso_credenciales(profesores)
            if validacion:
                print(mensaje)
            else:
                print(mensaje)
                continue
            ingreso_profesor(profesor)
        elif int(opt) == 3:
            for curso in cursos:
                print(f"{curso} Carrera: Tecnicatura Universitaria en Programación")
        elif int(opt) == 4:
            respuesta = "salir"
        else: print("Ingrese una opción válida.")
    else: 
        print("Ingrese una opción numérica.")
    
    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")











