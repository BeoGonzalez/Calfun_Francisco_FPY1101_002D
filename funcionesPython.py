#Funciones hechas por Benjamin Montoya, Vicente Ruiz y Benjamín Gonzalez
#Funcion para agregar libros  
libros=[]

def agregar_libro():
    print("A seleccionado agregar un libro")
    libro=input("Escriba el libro que desea agregar---> ")
    autor=input("Ingrese el autor--->")
    año=input("Ingresa el año de publicación del libro---> ")
    genero=input("Ingrese el genero del libro---> ")
    titulo={'TITULO':libro,
            'AUTOR':autor,
            'AÑO DE PUBLICACION':año,
            'GENERO':genero}
    libros.append(titulo)

    

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
        modificar=input("¿Cual libro desea modificar? ")
        if modificar in libros:
            opcion=int(input("¿Que desea modificar?\n1)Libro\n2)"))

def eliminar_libro():
    if not libros:
        print("No hay libros en la libreria")
    else:
        print("A seleccionado eliminar un libro")
        for i in libros:
            libro=input("Ingresa el libro que desea eliminar: ").lower()
            if libro in libros:
                libros.remove(libro)
                del(libro)
             

def guardar_archivo():
    if not libros:
        print("No hay libros en la libreria")
        return
    
                
            

    