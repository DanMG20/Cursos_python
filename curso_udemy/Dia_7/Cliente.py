from Persona import Persona
class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = 0
    
    def __str__(self):
        decoradores = "-"*30
        informacion_cliente = decoradores +f"""
Información del cliente: 
Nombre: {self.nombre}
Apellido: {self.apellido}
Numero de cuenta : {self.numero_cuenta}
Balance : {self.balance}
""" + decoradores
        return informacion_cliente
    
    
    def depositar(self,cantidad_deposito):
        self.balance +=cantidad_deposito
 
    def retirar(self,cantidad_retiro): 
        if self.balance ==0: 
            print(f"Lo siento tu saldo es {self.balance}, agrega fondos primero para poder retirar")
        elif self.balance< cantidad_retiro:
            print("El monto que deseas retirar es mayor a lo que tienes en tu balance, eso no es posible")
        else: 
            self.balance -= cantidad_retiro
            print(f"Retiro realizado con exito!, el saldo actual es: {self.balance}")

