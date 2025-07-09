import os
from pathlib import Path 
#obtener current working directory
ruta = os.getcwd()
print(ruta)
#cambiar ruta de trabajo 
ruta = os.chdir("C:\\Users\\EDMG0\Documents\\Proyectos_python\\curso_udemy\\Dia_6")
#sirve para crear una carpeta nueva 
archivo = open("archivo.txt","r")
print(archivo.read())
ruta = os.makedirs
print(ruta)



ruta ="C:\\Users\\EDMG0\Documents\\Proyectos_python\\curso_udemy\\Dia_6"

elemento = os.path.split(ruta)
print(elemento)

##para eliminar una carpeta 
os.rmdir("C:\\Users\EDMG0\\Documents\\Proyectos_python\\curso_udemy\\Dia_6\\d")

#para que cualquier sistema operativo lo pueda abrir
carpeta = Path("C:/Users/EDMG0/Documents/Proyectos_python/curso_udemy/Dia_6")
archivo = carpeta / "otro_archivo.txt"