#combina dos o mas listas en tuplas 
# llega al largo de la lista mas corta

ciudades = ["Lima","Madrid","Mexico","Barcelona"]

nombres = ["HUGO","VALERIA","ANA"]

edades = [65,29,42,12,45]


combinados = list(zip(nombres,edades,ciudades))

print(combinados)



for nombre, edad,ciudad in combinados: 
    print (f"{nombre} tiene {edad} años y vive en {ciudad} ")


uno= ["uno" , "um" , "one"]
dos= ["dos",  "dois","two"]
tres= ["tres" , "três","three"]
cuatro= ["cuatro", "quatro","four"]
cinco =  ["cinco", "cinco", "five"]

