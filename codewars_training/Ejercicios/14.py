"""

In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
"""
numeros = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"
def high_and_low(numbers):
    num_separados = []
    num_separados =numbers.split(" ")
    numeros_int =[]
    for numero in num_separados: 
        numeros_int.append(int(numero))

    return f'{max(numeros_int)} {min(numeros_int)}'


print(high_and_low(numeros))