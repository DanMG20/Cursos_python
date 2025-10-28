
"""
Devuelve el número (conteo) de vocales en la cadena dada.

Consideraremos a, e, i, o, u como vocales para esta kata (pero no y).

La cadena de entrada solo constará de letras minúsculas y/o espacios.
"""

cadena =" Tres tristes tigres comen trigo en un trigal"


def contador_vocales(cadena):

    vocales= ["a","e","i","o","u"]
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador +=1
    return contador

print(contador_vocales(cadena))