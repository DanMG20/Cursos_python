""" FUNCIONALIDAD DEL PROGRAMA:
1.-usuario ingresa texto cualquiera
1.- (convertir todo a minusculas o mayusculas para compararlos)
2.- ingresar 3 letras a su eleccion
4.- hacer analisis  y colocar cuantas veces aparece esa letra en el texto
5.- cuantas palabras hay en todo el texto
6.- informar primer y ultima letra del texto
7.- enseñar texto invertido
8 .- si aparece la palabra python en el texto verificar 


"""

input_texto = input("Ingresa cualquier texto que quieras mi amor:")

letra_1 = input("ahora el primer caracter:")
letra_2 = input("ahora el segundo caracter:")
letra_3 = input("ahora el tercero caracter:")

texto_mayusculas = input_texto.upper()
letra_1_mayuscula =letra_1.upper()
letra_2_mayuscula =letra_2.upper()
letra_3_mayuscula =letra_3.upper()

contador_letra_1 = texto_mayusculas.count(letra_1_mayuscula)
contador_letra_2 = texto_mayusculas.count(letra_2_mayuscula)
contador_letra_3 = texto_mayusculas.count(letra_3_mayuscula)

cantidad_palabras = len(input_texto.split())


print("En tu texto el número de veces que aparece: \n"
        + letra_1 +":" + str(contador_letra_1)+ "veces \n"
      + letra_2 +":" + str(contador_letra_2) +"veces \n"
      + letra_3 +":" + str(contador_letra_3) +"veces" 
    )
print("el numero de palabras es: " + str(cantidad_palabras))
print("La letra inicial y final son:")
print("Letra inicial: "+input_texto[0] + "  "+"Letra final: "+input_texto[-1])

texto_alreves= input_texto[::-1]
print("El texto al revés es:" + texto_alreves)
existe_python = "Python" in input_texto
if existe_python == True: 
    print ("la palabra Python está en el texto")
else: 
    print ("la palabra Python no está en el texto")