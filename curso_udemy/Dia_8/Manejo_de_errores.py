"""
Ejemplo de resolución:

def nombre_funcion(argumento):
    try:
        {Lo que haría la función habitualmente}
    except:
        {Excepción}
    else:
        ... etc.
"""
#practica 1 


def suma(num1,num2):
    try:
        print(num1+num2)
    except:
        print("Error inesperado")
    
# practica 2 
def cociente(num1,num2):
        try: 
            print(num1/num2)
        except TypeError as e:
           print("Los argumentos a ingresar deben ser números")  
        except ZeroDivisionError as z: 
            print("El segundo argumento no debe ser cero")

# pracctica 3 


def abrir_archivo(nombre_archivo):
    
    try:
        archivo = open(nombre_archivo)
        print("Abriendo exitosamente")
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    else:
        print("Error desconocido")

    finally: 
        print("Finalizando ejecución")
