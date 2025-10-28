from random import randint
def lanzar_dados(): 
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return dado1,dado2



def evaluar_jugada(dado1,dado2):
    suma = dado1+dado2
    if suma <=6: 
        return  f"La suma de tus dados es {suma}. Lamentable"
    elif 10>suma>6:
        return  f"La suma de tus dados es {suma}. Tienes buenas chances"
    else: 
        return  f"La suma de tus dados es {suma}. Parece una jugada ganadora"
    
dado1,dado2 = lanzar_dados()
resultado= evaluar_jugada(dado1,dado2)
print(resultado)

### 2
lista_numeros = [1,2,15,7,2]

def reducir_lista(lista_numeros): 
    mi_set=set()
    lista_nueva=[]
    for numero in lista_numeros:  
        mi_set.add(numero)
    for numero in mi_set:
        lista_nueva.append(numero)
    lista_nueva.pop(lista_nueva.index(max(lista_nueva)))
    return lista_nueva

def promedio(lista_nueva):
    suma=0
    for indice,numero in enumerate(lista_nueva): 
        suma = suma + numero 
    cantidad_numeros = indice + 1 
    prom = suma/(cantidad_numeros)
    return prom
print(reducir_lista(lista_numeros))
resultado= promedio(reducir_lista(lista_numeros))
print(resultado)



## practica 3 

lista_numeros = [1,2,3,4,5,6]
def lanzar_moneda():
    resultado = randint(1,2)
    if resultado == 1: 
        return "Cara"
    elif resultado ==2: 
        return "Cruz"

def probar_suerte(resultado_moneda,lista_numeros):
    if resultado_moneda =="Cara":
        print("La lista se autodestruira")
        del(lista_numeros)
        return lista_numeros
    elif resultado_moneda =="Cruz": 
        print("La lista fue salvada")
        return lista_numeros