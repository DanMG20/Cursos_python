class Numeros:
    def __init__(self,area):
        self.area = area
        self.contador = 0 


    def generador_turno(self):
        while True: 
            self.contador += 1 
            yield f"Tu turno es: {self.area}-{self.contador}"


