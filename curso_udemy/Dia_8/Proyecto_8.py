"""
Hacer un generador de turnos : 
pregunta al cliente a que area se dirige
3 areas farmacia cosmeticos perfumeria

dividir en dos modulos
numeros 
principal 

"""
from numeros import Numeros

#--------------------------------funciones----------------------------------------

def decorador(): 
    print("-"*30)

def seleccion_area(): 
    decorador()
    print(""" Bienvenido al Menú,
          [F] Farmacia
          [C] Cosméticos
          [P] Perfumeria
          [S] Salir""")
    decorador()
    decision =0
    while decision not in ["F","C","P","S"]:
        decision = input("A que área deseas dirigirte?[F,C,P,S]:")
    return decision

def menu(decision,objetos):
    if decision == "F":
       
        print(next(objetos[1].generador_turno()))
        input("Presiona Enter para volver al Menu")


    elif decision == "C":
        
        print(next(objetos[0].generador_turno()))
        input("Presiona Enter para volver al Menu")


    elif decision == "P":
        
        print(next(objetos[2].generador_turno()))
        input("Presiona Enter para volver al Menu")


    else: print(" El programa a finalizado")
    
def generar_objetos():
     obj_farmacia = Numeros("F")
     obj_cosmeticos = Numeros("C")
     obj_perfumeria = Numeros("P")
     return obj_cosmeticos,obj_farmacia,obj_perfumeria
#--------------------------------main----------------------------------------
objetos=generar_objetos()
decision = -1 
while decision != "S": 
    decision = seleccion_area()
    menu(decision,objetos)
    