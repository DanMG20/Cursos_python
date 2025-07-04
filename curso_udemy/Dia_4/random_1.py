# Numeros aleatorios 
from random import *


aleatorio = randint(1,50)
print(aleatorio)

# numero aleatorio con decimales
aleatorio_2 = uniform(1,5)


#Numero entre 0 y 1 
aleatorio_3 = random()

# Elige un numero aleatorio en la lista
colores = ["azul","blanco","rojo","negro"]
aleatorio_5 = choice(colores)
# shuffle para mezclar una lista 
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)