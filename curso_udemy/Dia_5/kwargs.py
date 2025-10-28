#keyword args solo se necesita que tenga dos asteriscos ** 
# se pueden escribir tantos argumentos como se requieran, pero a la vez permite darle un nombre a cada uno de los argumentos
# y ubicarlos en un diccionario 
#Practica 1
diccionario ={"clave_1":10,"clave_2":15,"clave_3":20}
def cantidad_atributos(**kwargs):
        for indice,kwarg in enumerate(kwargs):
            continue
        return indice+1


print(cantidad_atributos(**diccionario))


#practica 2

def lista_atributos(**kwargs):
      lista=[]
      for value in kwargs:
        lista.append(kwargs.get(value))
        print(kwargs.get(value))
      return lista
      

print(lista_atributos(**diccionario))


#practica 3


def describir_persona(nombre,**kwargs):
     print(f"Caractéristicas de {nombre}")
     for key,value in kwargs.items():
          print(f"{key}:{value}")


describir_persona("Edgar",**diccionario)


