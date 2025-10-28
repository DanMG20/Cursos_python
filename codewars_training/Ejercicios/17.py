"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""
numbers = [1, 0, 1, 2, 0, 1, 3]

def move_zeros(lst):
    for digito in lst: 
        if digito == 0:
            lst.remove(digito)
            lst.append(digito)
        
    return lst



print(move_zeros(numbers))