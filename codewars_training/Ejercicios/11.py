"""
Tu objetivo es escribir una función que elimine el primer y el último carácter de una cadena.
 Se te da un parámetro: la cadena original.

Importante: Tu función debe manejar cadenas de cualquier longitud ≥ 2 caracteres. 
Para cadenas con exactamente 2 caracteres, devuelve una cadena vacía.
"""
string = "to"
def remove_char(s):
    if len(s) == 2: 
        return ""
    else : 
        resultado = ""
        for  indice,letra in enumerate(s):
            if indice >0 and indice<len(s)-1: 
                resultado += letra
        return resultado
    

print(remove_char(string))



