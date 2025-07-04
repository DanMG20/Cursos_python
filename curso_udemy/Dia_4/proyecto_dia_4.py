"""
1.- preguntar al usuario su nombre 
2.- pensar numero entre el 1 y 100 
3.- 8 intentos para adivinar
4.- el programa responde 4 respuestas distintas 
a)Numero no permitido 
b)Incorrecto menor 
c)Incorrecto mayor 
d)Acertó cuantos intentos le tomó 

"""

from random import randint

numero_aleatorio =randint(1,101)
intentos =8
print(numero_aleatorio)
nombre = input("Hola bb pasame tu nombre ajaja que bonitos ojos:")
numero = int(input(f"{nombre},Ahora piensa en un numero entre el 1 y el 100, tienes 8 intentos para adivinar:"))
while intentos>0: 
    if numero > numero_aleatorio: 
        intentos-=1
        numero = int(input(f"{nombre},Papirriqui, el numero que me diste es mayor al que buscas te quedan {intentos} intentos: "))
    elif numero < numero_aleatorio: 
        intentos-=1
        numero= int(input(f"{nombre},Papirriqui, el numero que me diste es menor al que buscas te quedan {intentos} intentos: "))
    elif  numero_aleatorio==numero: 
        print(f"{nombre},Hay cabron eres el mero ruffle de mis papas adivinaste el numero {numero_aleatorio} en tan solo {intentos} intentos")
        break
    else: 
        print(f"{nombre},No te pases de verga e we, te dije que un numero entre 1 y 100")