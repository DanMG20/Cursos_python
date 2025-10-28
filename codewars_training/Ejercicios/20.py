"""
Your task, is to create N×N multiplication table, of size provided in parameter.

For example, when given size is 3:

[[1,2,3],[2,4,6],[3,6,9]]

pseudo: 


1st number row 
2nd columns 


"""





size = 3
def multiplication_table(size):
    rows = []
    indice = 0
    for column_index in range(size):
        row=[]
        for row_index in range(size):
            indice = (row_index+1)*(column_index+1)
            row.append(indice)
        rows.append(row)
    return rows

print(multiplication_table(size))

"""
    for column in range(size[1]):
print( f' column: {column}')
row =[]

            row.append(indice)
rows.append(row_index)
print(rows)
"""



