#los caracteres de las cadenas de texto estan indizados
# index sirve para buscar si hay un caracter en especifico en la cadenna de texto

texto = "Esta es una prueba"
#busca la a de izq  a derecha
resultado = texto.index("a")
resultado2= texto[0]
#busca de derecha a izq
resultado3 = texto.rindex("a")
print(resultado)
print(resultado2)
print(resultado3)