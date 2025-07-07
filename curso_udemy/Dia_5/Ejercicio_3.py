
argumentos= (0,0,3,1,2,6,1,1)
def detectar_2_00(*args):
    indice_ceros = []
    for indice,arg in enumerate(args):
            if arg == 0: 
                  indice_ceros.append(indice)
            
    
    if 1>=len(indice_ceros)>=0:
          
          return False
    elif indice_ceros[0]-indice_ceros[1] ==-1:
          return True
    else:
          return False

print(detectar_2_00(*argumentos))


