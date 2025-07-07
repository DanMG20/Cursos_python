#args es una palabra o funcion que se utiliza para pasar una cantidad no definida de argumentos a una funcion 
# Muy util si no sabes cuantos argumentos exactamente tiene que pasar 
# se define solo con el asterisco args se coloca nadamas para saber que pedo

def suma(*args):
    suma = 0
    for numero in args: 
        suma +=numero
    return suma 
    

print(suma(1,2,3,4,5,6,67))


#Practica 1 

def suma_cuadrados(*args): 
    suma=0
    for arg in args: 
        suma += arg**2
    return suma 

#practica 2 

def suma_absolutos(*args):
    suma=0
    for arg in args:
        suma += abs(arg)
    return suma 

#practica 3 
def numeros_persona(nombre,*args):
    suma_numeros=0 
    for arg in args: 
        suma_numeros += arg
    return f"{nombre}, la suma de tus números es {suma_numeros}"

