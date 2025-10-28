

def funcion_ordenar(palabra):
    mi_set = set()
    lista_palabra = []
    for letra in palabra:
        mi_set.add(letra)
    for letra in mi_set:
        lista_palabra.append(letra)
    lista_palabra.sort()
    return lista_palabra

print(funcion_ordenar("entretenido"))
