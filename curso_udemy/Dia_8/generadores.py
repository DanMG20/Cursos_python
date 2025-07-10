"""
DIseñandas para aprovechar mejor el espacio de memoria en funcion de que lo vas necesitando 
"""

def mi_funcion (): 
    yield 4 


print(mi_funcion)
g = mi_funcion()

print(next(g))



def mi_generador(): 
    for x in range (1,5): 
        yield x*10



print(mi_generador())
f = mi_generador()
print(next(f))



# practica 1 
def generador():
    x=0
    while True: 
        x+=1
        yield x


generador = generador()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
# practica 2

def multiplos_7():
    x=0 
    while True: 
        x+=1
        yield 7*x

multiplo_7 = multiplos_7()

print(next(multiplo_7))


print(next(multiplo_7))
print(next(multiplo_7))
print(next(multiplo_7))
print(next(multiplo_7))
print(next(multiplo_7))

#practica 3 


def contador_vidas():
    vidas =4 
    while vidas!=1:
        vidas-=1
        if vidas >1:
            yield (f"Te quedan {vidas} vidas")
        elif vidas ==1:
                yield "Te queda 1 vida"
    yield "Game over"

perder_vida = contador_vidas()

print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))