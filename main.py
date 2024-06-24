#ingresar libreria
import time
import funcionesPython as funcion
#Hecho por Benjamin Montoya, Vicente Ruiz y Benjamín Gonzalez
#Menu de opciones
while True:
    print("---Bienvenido a la Libreria DUOC---")
    print("1.- Agregar un libro.")
    print("2.- Ver todos los libros.")
    print("3.- Modificar libro.")
    print("4.- Elimina un libro.")
    print("5.- Guardar coleccion en un archivo.")
    print("6.- Salir del programa.")
    try:
        opcion=int(input("Seleccione una opcion: "))
    except ValueError:
        print("Ingrese una opcion valida.")
    if (opcion==1):
        funcion.agregar_libro()
    elif (opcion==2):
        funcion.ver_libros()
    elif (opcion==3):
        funcion.modificar_libro()
    elif (opcion==4):
        funcion.eliminar_libro()
    elif (opcion==5):
        funcion.guardar_archivo()
    elif (opcion==6):
        break
    else:
        print("ERROR ingresa una opción valida")
