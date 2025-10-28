"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If a number is a multiple of both 3 and 5, only count it once.
"""


numero = 10

def solution(number):
    result = 0
    if number <0:
        return 0
    else:

        for numero in range(1,number):
            if numero%3==0 or numero%5==0: 
                result+=numero
        return(result)

print(solution(numero))
