class Pajaro : 
    alas = True 
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
        

    def piar (self):
        print("pio")

    
    def volar (self, metros):
        print(f"El pajaro ha volado {metros} metros")


piolin = Pajaro("Amarillo","Canario")
piolin.piar()
piolin.volar(20)



# practica 1 

class Perro: 

    def ladrar(self):
        print("Guau!") 


perro = Perro.ladrar


# practica 2 

class Mago: 

    def lanzar_hechizo(self): 
        print("¡Abracadabra!")

merlin = Mago.lanzar_hechizo

#practica 3 

class Alarma:
    def postergar(self,cantidad_minutos): 
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")


alarma1 = Alarma.postergar(15)