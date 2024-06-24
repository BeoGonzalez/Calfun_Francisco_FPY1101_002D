import time
import funcionesPython as funcion

while True:
    print("---Bienvenido a la libreria DUOC---")
    print("1.- Agregar un libro.")
    print("2.- Ver todos los libros.")
    print("3.- Elimina un libro.")
    print("4.- Guardar coleccion en un archivo.")
    print("5.- Salir del programa.")

    opcion=input("Seleccione una opcion")
    if (opcion==1):
        funcion.agregar_libro
    elif (opcion==2):
        funcion.ver_libros
    elif (opcion==3):
        funcion.eliminar_libro
    elif (opcion==4):
        funcion.guardar_archivo
    elif (opcion==5):
        funcion.guardar_archivo
    else:
        print("ERROR ingresa una opción valida")
