"""

Create a function that takes a Roman numeral as its argument and returns 
its value as a numeric decimal integer. 
You don't need to validate the form of the Roman numeral.


I          1
V          5
X          10
L          50
C          100
D          500
M          1,000

"MDCLXVI" -> 1666

I = 1
II = 2
III = 3 
IV = 4
V = 5
VI = 6
VII = 7
VIII = 8 
IV = 9 
X = 10 
"""


numero = "MDCLXIIV" 

def solution(roman_number):

    conversion = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000,
        }
    result= 0
     # si un numero menor esta después del mayor se suma 
     
    for indice,numero_ro in enumerate(roman_number): 
        if indice == 0:
            result += conversion.get(numero_ro)
        elif numero_ro[indice-1] < numero_ro:
       
            result -= conversion.get(numero_ro)
        elif numero_ro in conversion.keys():
            result += conversion.get(numero_ro)
        
    return result
    # si un un numero menor esta detras del mayor se resta a este 
   
## INCOMPLETO ##

solution(numero)