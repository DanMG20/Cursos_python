"""
Tu tarea consiste en encontrar todos los elementos no consecutivos de un array.

Un número no es consecutivo si no es exactamente uno mayor que el elemento anterior del array.
 El primer elemento pasa y nunca se considera no consecutivo.

Crea una función llamada all_non_consecutive.

Por ejemplo, si tenemos un array [1,2,3,4,6,7,8,15,16], entonces 6 y 15 no son consecutivos.

Debes devolver los resultados como un array de objetos con dos valores: i: <el índice del número no consecutivo> y
 n: <el número no consecutivo>.


"""

arr = [1,2,3,4,6,7,8,15,16]

def all_non_consecutive(arr):
    impostores = []
    for indice,numero in enumerate(arr): 
        if indice == 0: 
            continue

        elif (arr[indice-1]+1) == (numero): 
            continue
        else: 
            impostores.append({'i': indice, 'n': numero})

    return impostores

print(all_non_consecutive(arr))

    