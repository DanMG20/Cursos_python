"""
U cuesta arriba 
D cuesta abajo 


Montaña = n veces U terminando con D 
Valle  =  n veces D terminando con U

¿Cuantos valles camino?



ejemplo  8 pasos = [DDU- UUUD-D]



"""
pasos = 8
camino = "DDUUUUDD"
def contandoValles(pasos, camino): 
# si el paso cambia  de D = cuesta abajo, a U = cuesta arriba entonces lugar =  Valle 
# si el paso cambia de U = cuesta arriba, a D = cuesta abajo entonces lugar = montaña 
    valles = 0
    nivel = 0  # (nivel del mar)  

    for paso in camino: 
        if paso == "U": 
            nivel +=1
            if nivel == 0:
                valles +=1
        else: 
            nivel -=1
    return valles


print(contandoValles(pasos,camino))


"""
SI  numero == 0  puedes saltar sobre el, 
SI  numero == 1 no puedes saltar sobre el 

solo podemos dar saltos de 1 o 2
tenemos 

[0,1,0,0,0,1,0]

contador = 0 
SI contador >= len(c)
    if  siguiente numero == 1: 
    salto =2
    elif el siguiente del siguiente == 1: 
    salto = 1
    else :
    salto = 2 



"""


