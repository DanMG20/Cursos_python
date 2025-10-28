"""
Escriba una función que tome una cadena de una o más palabras y la devuelva, 
pero con todas las palabras que tengan cinco o más letras invertidas 
(como el nombre de esta kata). 
Las cadenas pasadas consistirán únicamente en letras y espacios. 
Los espacios se incluirán solo cuando haya más de una palabra."""


string = "Hey fellow warriors"


def funcion_voltiar(string): 
    palabras = string.split()
    palabras_reordenadas = []

    for palabra in palabras: 
        if len(palabra)>=5: 
            palabra_invertida =(palabra[::-1])
            palabras_reordenadas.append(palabra_invertida)

        else:
            palabras_reordenadas.append(palabra)
    nueva_frase = " ".join(palabras_reordenadas)
    print(palabras_reordenadas)
    return nueva_frase





