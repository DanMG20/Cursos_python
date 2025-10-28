


place = 0
saltos = 0

c= [0,1,0,0,0,1,0]

while place < len(c)-1:
    if place+2 < len(c) and c[place + 2 ] == 0: 
        place +=2
    else: 
        place +=1
    saltos +=1


print(saltos)