"""
1.- Saludar 
2.- Dar la dirección de las recetas 
3.- Dar el numero de recetas en total 
4.- Desplegar el menu: 
1) -leer receta 
    -elegir categoria 
    -mostrar recetas
    elegir receta
    -leer receta
2) -crear receta
    -elegir categoria 
    -crear nombre 
    -crear contenido 
3) -crear categoria
    -solicita nombre categoria
    -crear categoria 
4) eliminar receta
   -elegir categorpia 
    -mostrar recetas
    elegir receta
    -eliminar receta
5) eliminar categoria
    -preguntar categoria a eliminar 
6) finalizar programa 


"""
from os import system
from pathlib import Path
#-----------------------------------------------Funciones------------------------------------------------------

def saludar(): 
    print("-"*40+"| "+"Hola! este es el recetario"+" |"+"-"*40)

def dir_num_recetas(ruta_recetario_principal):
    cantidad_recetas = 0
    for receta in Path(ruta_recetario_principal).glob("**/*.txt"):
        cantidad_recetas+=1
    print ("La ruta donde encontrarás todas las recetas de este programa es:")
    print("-"*20+"| "+str(ruta_recetario_principal)+" |"+"-"*20)
    print(f"Ahora mismo existen {cantidad_recetas} recetas")
    
def mostrar_menu(): 
    print("-"*40+"| "+"MENU"+" |"+"-"*40)
    print ("""
        [1] Leer receta 
        [2] Crear receta
        [3] Crear categoria 
        [4] Eliminar receta
        [5] Eliminar categoria
        [6] Finalizar programa \n""")
    
def seleccionar_opcion():
    mostrar_menu()
    opciones =["1","2","3","4","5","6"]
    seleccion = 0
    while seleccion not in opciones: 
        seleccion = input("Porfavor selecciona una opción [1-6]:  ")
        system("cls")
        if seleccion =="6":
            print("El programa a finalizado")
        
    return seleccion


def mostrar_y_seleccionar_categoria(ruta_recetario_principal):
    seleccion_categoria=-1
    subdirectorios = []
    indices = []
    print("Las categorias se muestran a continuación:  ")
    for indice,subdirectorio in enumerate(ruta_recetario_principal.iterdir()):
        subdirectorios.append(subdirectorio)
        indices.append(str(indice))
        print(f"[{indice}] {subdirectorio.name}")
    while seleccion_categoria not in indices:
        seleccion_categoria =input(f"Selecciona la categoría de la receta[{min(indices)}-{max(indices)}]:")
    system("cls")
    return seleccion_categoria,subdirectorios

def mostrar_y_selecc_recetas(seleccion_categoria, subdirectorios,ruta_recetario_principal):
    seleccion_receta =-1
    recetas =[]
    indices = []
    for indice,receta in enumerate(subdirectorios[int(seleccion_categoria)].iterdir()):
        recetas.append(receta)
        indices.append(str(indice))
        print(f"[{indice}] {receta.stem}")
    if indices == []:  
        print ("No existe ninguna receta en este directorio aún")
    else:

        while seleccion_receta not in indices:
            seleccion_receta=input(f"Selecciona la receta[{min(indices)}-{max(indices)}]:")
    system("cls")
    return seleccion_receta,recetas

def salir_al_menu():
    input("Presiona Enter para salir al menu: ")
    system("cls")
def leer_receta(seleccion_receta,recetas):
    print (f"Estás leyendo el contenido de la receta: {recetas[int(seleccion_receta)].stem}")
    print(recetas[int(seleccion_receta)].read_text())


def crear_receta (seleccion_categoria,subdirectorios):

    receta_existe = None
    while receta_existe == None: 
        nombre_receta = input ("Introduce el nombre que deseas poner a tu nueva receta:")
        nueva_receta =Path(subdirectorios[int(seleccion_categoria)],nombre_receta+".txt")

        if nueva_receta.exists():
            print("Esta receta ya existe, ponle otro nombre porfavor")
            receta_existe = None
        else:
            print(f"Tu receta :{nueva_receta.stem} ha sido creada con exito")
            nueva_receta.touch()
            receta_existe = True
    contenido_receta = input("Excelente!, Ahora agrega el contenido de la receta: ")
    nueva_receta.write_text(contenido_receta)
    print("Tu receta ha sido escrita y guardada con exito!")


def eliminar_receta(seleccion_receta,subdirectorios):
    print (f"La receta ha sido eliminada: {recetas[int(seleccion_receta)].stem}")
    recetas[int(seleccion_receta)].unlink()

def eliminar_categoria(seleccion_categoria,subdirectorios):
    print (f"La categoria ha sido eliminada: {subdirectorios[int(seleccion_categoria)].stem}")
    subdirectorios[int(seleccion_categoria)].rmdir()
def crear_categoria(ruta_recetario_principal):
    categoria_existe = None
    while categoria_existe == None: 
        nombre_categoria = input ("Introduce el nombre que deseas poner a tu nueva categoria:")
        nueva_categoria =Path(ruta_recetario_principal,nombre_categoria)

        if nueva_categoria.exists():
            print("Esta categoría ya existe, ponle otro nombre porfavor")
            categoria_existe = None
        else:
            print(f"Tu categoria :{nueva_categoria.name} ha sido creada con exito")
            nueva_categoria.mkdir()
            categoria_existe = True
#-----------------------------------------------variables------------------------------------------------------
ruta_recetario_principal = Path("C:/Users/EDMG0/Documents/Proyectos_python/curso_udemy/Dia_6/Recetas")
seleccion_menu = None
#-----------------------------------------Programa-principal------------------------------------------------------

#ejecutamos la funcion saludo 
saludar()
#ejecutamos la funcion dar direccion
dir_num_recetas(ruta_recetario_principal)
#muestra el menu 
#selecciona una opcion y se asegura de que sea una opcion viable
seleccion_menu=seleccionar_opcion()
#inicia el loop para iniciar la seleccion del programa
while seleccion_menu !="6":
    if seleccion_menu =="1": 
        print("-Estas en la opcion \"Leer Receta\"[1]-")
        seleccion_categoria,subdirectorios=mostrar_y_seleccionar_categoria(ruta_recetario_principal)
        seleccion_receta,recetas=mostrar_y_selecc_recetas(seleccion_categoria,subdirectorios,ruta_recetario_principal)
        leer_receta(seleccion_receta,recetas)
        salir_al_menu()
        seleccion_menu=seleccionar_opcion()
        
    if seleccion_menu =="2": 
        print("-Estas en la opcion \"Crear Receta\"[2]-")
        seleccion_categoria,subdirectorios=mostrar_y_seleccionar_categoria(ruta_recetario_principal)
        crear_receta(seleccion_categoria,subdirectorios)
        salir_al_menu()
        seleccion_menu=seleccionar_opcion()
    if seleccion_menu =="3": 
        print("-Estas en la opcion \"Crear Categoría\"[3]-")
        crear_categoria(ruta_recetario_principal)
        salir_al_menu()
        seleccion_menu=seleccionar_opcion()
    if seleccion_menu =="4": 
        print("-Estas en la opcion \"Eliminar Receta\"[4]-")
        seleccion_categoria,subdirectorios=mostrar_y_seleccionar_categoria(ruta_recetario_principal)
        seleccion_receta,recetas=mostrar_y_selecc_recetas(seleccion_categoria,subdirectorios,ruta_recetario_principal)
        eliminar_receta(seleccion_receta,recetas)
        salir_al_menu()
        seleccion_menu=seleccionar_opcion()
        
    if seleccion_menu =="5": 
        print("-Estas en la opcion \"Eliminar Categoria\"[5]-")
        seleccion_categoria,subdirectorios=mostrar_y_seleccionar_categoria(ruta_recetario_principal)
        eliminar_categoria(seleccion_categoria,subdirectorios)
        salir_al_menu()
        seleccion_menu=seleccionar_opcion()