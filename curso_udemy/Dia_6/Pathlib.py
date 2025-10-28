from pathlib import Path 

carpeta = Path("C:/Users/EDMG0/Documents/Proyectos_python/curso_udemy/Dia_6/Recetas")
print(carpeta.name)

print(carpeta.stem)
for directorio in carpeta.iterdir():
    print(directorio)
    print(type(directorio))