#Son inmutables es decir no se pueden cambiar
#Ocupan menos espacio de memoria

mi_tuple =(1,2,(10,20),4)
tupla = (5,5.6, "hola", 12)


print(mi_tuple[2][1])


print((mi_tuple.index(1)))
mi_lista=[]
for elemnto in tupla:
    mi_lista.append(elemnto)

print(mi_lista)