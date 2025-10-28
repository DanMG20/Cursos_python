"""
¡Los trolls están atacando tu sección de comentarios!

Una forma común de abordar esta situación es eliminar todas las vocales de los comentarios de los trolls, neutralizando así la amenaza.

Tu tarea consiste en escribir una función que tome una cadena y devuelva una nueva cadena sin todas las vocales.

Por ejemplo, la cadena "¡Este sitio web es para perdedores, jajaja!" se convertiría en "¡Este sitio web es para perdedores, jajaja!".

Nota: para esta kata, la "y" no se considera una vocal.


"""
cadena = " Como me gusta la cuka ujujajja"

def disemvowel(string_):
    nueva_cadena = ''
    for letra in string_: 
        if letra not in 'aeiouAEIOU':
            nueva_cadena += letra


    return nueva_cadena


print(disemvowel(cadena))