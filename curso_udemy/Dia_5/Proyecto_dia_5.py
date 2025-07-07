""" 
1.- el programa elige una palabra secreta 
2.-Muestra una serie de guiones que indican el largo de la palabra
3.-El usuario indica una letra y si la letra esta en la palabra se descubre
4.- Por simplicidad tiene 6 vidas cada que elija una letra que no exista 

"""

from random import choices

def eleccion_palabra(): 
    palabras= ["COMER","APOCALIPSIS","TRASTORNADO","GLADIADOR","JAGUAR"]
    palabra_lista = choices(palabras, k=1)
    palabra = palabra_lista[0]
    palabra_incompleta = []
    for letra in palabra:
        palabra_incompleta.append("_")
    return palabra,palabra_incompleta


def mostrar_seleccion(eleccion_palabra):
    print("La longitud de la palabra es: \"", end="")
    for letra in eleccion_palabra: 
        print("_",end="")
    print("\"",end="")


def comparar_letras(letra_intento,palabra,palabra_incompleta):
    contador = 0 
    print("\"",end="")
    for indice,letra in enumerate(palabra): 
        if letra == letra_intento.upper() and palabra_incompleta[indice] =="_": 
            contador +=1
            palabra_incompleta.insert(indice,letra_intento)
            palabra_incompleta.pop(indice+1)
    for n in range(len(palabra)):
        print(palabra_incompleta[n],end="")
    print("\"",end="")
    return contador,palabra_incompleta



palabra,palabra_incompleta=eleccion_palabra()
intentos = 6
print(f"Bienvenido al juego del ahorcado, debes adivinar la palabra oculta y cuentas con {intentos} restantes:")
mostrar_seleccion(palabra)
letra_intento = input("\n Para comenzar ingresa una letra que creas que puede estar en la palabra:")
contador,palabra_incompleta=comparar_letras(letra_intento,palabra,palabra_incompleta)
while intentos-1>0:
    if "_" not in palabra_incompleta: 
        print("\nListo!, Ganaste!")
        break
    elif intentos ==1: 
        print("\n suerte para la siguente, chao")
        break
    else:
        if contador == 0:
            print("\n La letra que ingresaste no esta en la palabra")
            intentos-=1
            letra_intento= input(f"\n  tienes aún {intentos} intentos, ahora ingresa otra letra:")
            contador,palabra_incompleta = comparar_letras(letra_intento,palabra,palabra_incompleta)
        else:
            letra_intento= input(f"\n Ecxcelente! tienes aún {intentos} intentos, ahora ingresa otra letra:")
            contador,palabra_incompleta= comparar_letras(letra_intento,palabra,palabra_incompleta)
