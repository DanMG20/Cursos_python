"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0.
Note: If the number is a multiple of both 3 and 5, only count it once.
"""




def solution(number):
    if int(number) < 0:
        x=0
    else:
        numeros = list(range(3, int(number), 3))
        numero2 = list(range(5, int(number), 5))
        numer3 =[]
    for numero in numeros:
        if numero in numero2:
            print("numero repetido" + str(numero))
        else:
            numer3.append(numero)
            print(numer3)
            x=sum(numer3)
    return x

numero=input("Ingresa un numero")
x=solution(numero)
print(x)