#Crear buscador de numeros de serie 
#no hay mas de un numero de serie por archivo 
#-[N]+[tres caracteres de texto] } [-]+ [5 numeros]
# debe imprimir en formato tabla 
import re
from datetime import datetime
import os 
import time
import math


text = "Nryu-12365"

fecha_hoy = datetime.today()

def numero_serie_comparador(texto): 
    patron = (r"N[A-Za-z]{3}-\d{5}")
    resultado = re.search(patron,texto)
    
    if resultado: 
        return resultado.group()
    else:
        return None


def imprimir_tabla(fecha_hoy,folios_dic,tiempo_ejecucion): 
    print("-"*50)
    print(f"Fecha de búsqueda:{fecha_hoy.date()}")
    print("-"*50)
    print("Archivo \t\t | Número de serie")
    print("-"*50)
    for archivo,valor in folios_dic.items(): 
        print(f"{archivo} \t\t | {valor}")
    print("-"*50)
    print(f"Folios encontrados: {len(folios_dic)}")
    print(f"Duración de la búsqueda: {math.ceil(tiempo_ejecucion)} s")
    print("-"*50)


def listar_directorios():
    archivos_folio = {}
    for dir_carpeta, dir_nombres, archivos  in os.walk("Proyecto+Dia+9\\Mi_Gran_Directorio"):

        for archivo in archivos:
            ruta_completa = os.path.join(dir_carpeta, archivo)
            with open(ruta_completa, encoding="utf-8")  as f :
                contenido = f.read()
                
                folio =numero_serie_comparador(contenido)
                if folio != None:
                    archivos_folio[archivo] = folio
                else:
                    continue
            
    return archivos_folio
inicio = time.perf_counter()
folios_dic = listar_directorios()
fin = time.perf_counter()
tiempo_ejecucion = fin - inicio

imprimir_tabla(fecha_hoy,folios_dic,tiempo_ejecucion)