"""
Bienvenido. En esta kata, se le pide que eleve al cuadrado cada dígito de un número y los concatene.

Por ejemplo, si ejecutamos 9119 en la función, el resultado será 811181, porque 9^2 es 81 y 1^2 es 1. (81-1-1-81)

Ejemplo n.° 2: Una entrada de 765 devolverá/debería devolver 493625 porque 72 es 49, 62 es 36 y 52 es 25. (49-36-25)

Nota: La función acepta un entero y devuelve un entero.

¡Que disfrutes programando!"""


num = 123453

def square_digits(num):
    cuadrados = []
    cadena = ''
    if type(num) is int:
        for digito in str(num): 
            cuadrados.append(int(digito)**2)
    for numero in cuadrados:
        cadena += str(numero)
    
    return (int(cadena))
    


print(type(square_digits(num)))