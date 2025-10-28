dado_verde = [1,2,3,4,5,6]

dado_rojo = [1,2,3,4,5,6]


conjunto_A = []
espacio_muestral = [ ]
evento_B = [ ]


evento_C =[]
def calcular_evento_A(): 

        
    for indice in dado_verde:
        
        for indic in dado_rojo: 

            
            espacio_muestral.append(f'{indice}+{indic}')


            if indice+indic > 8 : 
                conjunto_A.append(f'{indice}+{indic}')



def calcular_evento_B (): 
   
    for indice in dado_verde:
        
        for indic in dado_rojo: 
            if indice ==2  or indic == 2 : 
                evento_B.append(f'{indice}+{indic}')

    return evento_B


def calculcar_evento_C():
    for indice_verde in dado_verde:
        for indice_rojo in dado_rojo: 
            if indice_verde >4 : 
                evento_C.append(f'{indice_verde}+{indice_rojo}')

    return evento_C


calcular_evento_A()
calcular_evento_B()
calculcar_evento_C()


numero_resultados = len(espacio_muestral)

def calcular_interseccion(evento_1, evento_2): 

    interseccion = set()

    for resultado_evento1 in evento_1: 

        interseccion.add(resultado_evento1)
    for resultado_evento2 in evento_2: 
        interseccion.add(resultado_evento2)

    return interseccion


def calcular_probabilidad(evento, N):

    n= len(evento)

    probabilidad = n/N


    return round(probabilidad*100,3)  





evento_D = calcular_interseccion(conjunto_A,evento_C)

print("\n")
print(" Probabilidad Evento C ")
print (f"\t {calcular_probabilidad(evento_D,numero_resultados)}%")
print("\n")


