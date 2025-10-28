#for 

nombres = ["juana", "pablo"]

for n in nombres: 
    print ("Hola "+ n)





numeros = [1,2,3,4,5]

valor = 0 

for numero in numeros: 
    valor = 0 + numero 
    print(valor)

# Ejercicio 
suma_impar=0
suma_par=0
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
for numero in lista_numeros:
    if numero%2 == 0: 
        suma_par = suma_par+numero
    else: 
        suma_impar= suma_impar+numero

suma_pares= suma_par
suma_impares=suma_impar

print(suma_pares,suma_impares)