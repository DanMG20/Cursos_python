from os import system
palabra = input("Ingresa una palabra:")
system ("cls")
for letra in palabra:
    print(letra ,end="")



#practica 1 
from pathlib import Path
archivo = Path("C:/Users/EDMG0/Documents/Proyectos_python/curso_udemy/Dia_6/archivo.txt")
def abrir_leer(archivo):
    print(archivo.read_text())

abrir_leer(archivo)

#a la vieja usanza

def abrir_leer(ruta): 
    archivo = open(ruta, "r")
    print(archivo.read())
    archivo.close


# 2 

def sobrescribir(ruta_archivo): 
    archivo = open(ruta_archivo, "w")
    archivo.write("contenido eliminado")
    archivo.close


#3 

def registro_error(ruta_archivo):
    archivo = open(ruta_archivo, "a")
    archivo.write("se ha registrado un error de ejecución")
    archivo.close
    