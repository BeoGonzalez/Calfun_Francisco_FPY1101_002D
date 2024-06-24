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
        eliminar_libro=input("ingrese el libro a eliminar: ")
    if eliminar_libro in libros:
        libros.remove(eliminar_libro)
        print(libros)
    else:
        print(f"El libro '{eliminar_libro}' no está en la lista.")
             

def guardar_archivo():
    if not libros:
        print("No hay libros en la libreria")
    else:
        with open('Calfun_Francisco_FPY1101_002D/planilla libros','w',encoding='utf-8') as archivo:
            archivo.write(libros)
            for libro in libros:
                print(libro)
                
                
        
    