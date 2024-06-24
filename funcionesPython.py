libros=[]
#Funcion para agregar libros
def agregar_libro():
    print("A seleccionado agregar un libro")
    libro=input("Escriba el libro que desea agregar---> ")
    autor=input("Ingrese el autor--->")
    año=input("Ingresa el año de publicación del libro: ")
    titulo={'TITULO':libro}
    nombre={'AUTOR':autor}
    fecha={'AÑO DE PUBLICACION':año}
    libros.insert(0,0,titulo)
    libros.insert(1,0,nombre)
    libros.insert(2,0,fecha)

    

def ver_libros():
    if not libros:
        print("No hay libros en la libreria")
    else:
        print(f"La lista de libros es: \n{libros}")

def modificar_libro():
    if not libros:
        print("No hay libros en la libreria")
    else:
        print("A seleccionado modificar un libro")    

def eliminar_libro():
    if not libros:
        print("No hay libros en la libreria")
    else:
        print("A seleccionado eliminar un libro")
        libro=input("Ingresa el libro que desea eliminar: ")
        if libro in libros:
            libros.remove()

    