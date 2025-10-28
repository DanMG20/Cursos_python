"""
Complete la solución para que divida la cadena en pares de dos caracteres.
 Si la cadena contiene un número impar de caracteres, debe reemplazar el segundo carácter 
 faltante del último par con un guion bajo ('_')."""

"""
1.- Separar cadena en cadenas de 2 caracteres 
2.- si el ultimo caracter de la cadena es impar agregar un _ 

"""
cadena = "alfabetizacionese"



def solution(s): 
    caracteres=2
    longitud= len(s)
    if longitud%2==0:
        contador = 0 
        trozo = ""
        lista=[]
        for letra in s:
            if contador <2: 
                contador+=1
                trozo+=letra 

            if contador ==2: 
                contador=0
                lista.append(trozo)
                trozo=""
    else: 
        contador = 0 
        trozo = ""
        lista=[]
        for indice, letra in enumerate(s):
            if contador <2: 
                contador+=1
                trozo+=letra 
            if contador ==2: 
                contador=0
                lista.append(trozo)
                trozo=""
            if indice+1 == longitud and contador==1: 
                trozo+="_"
                lista.append(trozo)
    return lista

    
