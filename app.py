import os

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

#-----------------------------------------------App principal----------------------------------------------------
mensaje_bienvenida()
respuesta = ''

while respuesta != "salir":
    menu_principal()
    opt = input("\n Ingrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla
    if opt.isnumeric():
        if int(opt) == 1:
            #alumnos
            pass
        elif int(opt) == 2:
            #profesor
            pass
        elif int(opt) == 3:
            #mostrar cursos
            pass
        elif int(opt) == 4:
            respuesta = "salir"
        else: print("Ingrese una opción válida.")
    else: 
        print("Ingrese una opción numérica.")
    
    input("Presione cualquier tecla para continuar....") # Pausa

print("Hasta luego!.")











