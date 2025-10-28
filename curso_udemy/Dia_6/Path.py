from pathlib import Path 
#Devuelve una ruta absoluta
base = Path.home()
# Desarrolla un directorio pero no es un directorio 
guia = Path(base,"Barcelona", "Sagrada_Familia")
print(base)
print(guia)


#practica 2 

ruta = Path("Curso Python","Dia 6","practicas_path.py")
relativo = ruta.relative_to(Path("Curso Python"))
print(relativo)


#practica 3 

base = Path.home()
ruta = Path(base, "Curso Python", "Diá 6", "practicas_path.py")

print(ruta)