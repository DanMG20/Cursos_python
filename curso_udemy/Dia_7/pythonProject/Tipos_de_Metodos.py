class Pajaro : 
    alas = True 
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
        

    def piar (self):
        print("pio")

    
    def volar (self, metros):
        print(f"El pajaro ha volado {metros} metros")


#ejercicio 1
class Mascota: 

    @staticmethod
    def respirar(): 
        print("Inhalar... Exhalar")

#ejercicio 2
class Jugador: 
    vivo = False
    @classmethod
    def revivir(cls):
        cls.vivo =True

Jugador.revivir()

print(Jugador.vivo)

#ejercicio 3 


class Personaje: 

    def lanzar_flecha():
        cantidad_flechas = 2
        cantidad_flechas -=1

