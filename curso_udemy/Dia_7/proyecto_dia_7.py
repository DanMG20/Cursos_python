"""
clase Persona
atributos nombre  y apellido 
clase cliente(Persona)
 atributos numero _cuenta y balance 
 metodos para imprimr (todo)
-depositar()
-retirar()
----------------main-----------
codigo para elegir, Depositar, Retirar o salir
funciones
-crear_cliente()
-inicio()

"""
from os import system
from Cliente import Cliente

def crear_cliente(nombre,apellido,numero_cuenta):
    objeto_cliente = Cliente (nombre,apellido,numero_cuenta)
    return objeto_cliente

def inicio (cliente): 
    print(cliente)
    print(f"""Bienvenido,
[0] Depositar
[1] Retirar
[2] Salir
          """)


#Creacion del objeto cliente
cliente = crear_cliente("Pedro","Ramirez",1)
opciones =["0","1","2"]
opcion = " " 
while opcion !="2":
    inicio(cliente)
    opcion = input("Elige una opcion[0-2]: ")

    if opcion == "0": 
        system("cls")
        cantidad_deposito = float(input("Ingresa la cantidad que quieres depositar a tu saldo: "))
        cliente.depositar(cantidad_deposito)
        print(f"Deposito realizado con exito!, el saldo actual es: {cliente.balance}")
        input("Presiona Enter para regresar al Menú")
        system("cls")
        
    elif opcion == "1":
        system("cls")
        cantidad_retiro =  float(input("Ingresa la cantidad que quieres retirar de tu saldo: "))
        cliente.retirar(cantidad_retiro)
        input("Presiona Enter para regresar al Menú")
        system("cls")
    else:
        system("cls")
        print("El programa a finalizado")