#sirve para buscar o determinar un texto con determinado orden
# /d -digito numeroico 
# /w - caracter alfanumerico  (letra oo numero )
# /s espacio en blanco  
# /D no numerico 
# /W no alfanumerico  (solo signos)
# /S no espacio en blanco 
# cuantificafores 
# + 1 o mas veces 
# {n} se repite n veces
# {n,m} se repite entre n y m veces
# n, desde n hacia arriba 
# * 0 ó mas veces 
# ? 1 ó 0 

import re





#practica 1 

email = "usuario@host.com"
def verificar_email(email): 



    patron = r"\w{1,10}@\w{1,10}.com"
    resultado = re.search(patron,email)

    if resultado ==True: 
            print ("Ok")
    else: 
            print("La dirección de email es incorrecta")


verificar_email(email)


#practica 2 

saludo = "Hola, bebe"

def verificar_saludo(saludo):
    patron=(r"Hola\w +1")
    resultado = re.search(patron,saludo)
    if resultado ==True: 
        print ("Ok")
    else: 
        print("No has saludado")



verificar_saludo(saludo)

cp= "af1234"
def verificar_cp(cp):
    patron=(r"\w{2}\d{4}")
    resultado = re.search(patron,cp)
    if resultado ==True: 
        print ("Ok")
    else: 
        print("El código postal ingresado no es correcto")
          

verificar_cp(cp)