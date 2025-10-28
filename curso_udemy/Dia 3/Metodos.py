texto ="Este es el texto de Edgar"
# Elevar a mayusculas toda o solo una parte de la cadena de texto
resultado = texto[:4].upper()
#Separar el texto en una lista se puede elegir desde que letra separar
resultado = texto.split("t")




print(resultado)

a = "Aprender"
b= "Python"
#Metodo para unir elementos de una lista
e =" ".join([a,b])
print(e)

# Si no encuentra la letra regresa un -1
resultado2 = texto.find("f")
print(resultado2)

print (texto.replace("e","x"))

