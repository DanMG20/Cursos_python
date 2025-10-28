#atributos de clase  (Todos los objetos tienen los mismos atributos)
#atributos  de instancia ( Atributos que son distintos en cada instancia)

class Pajaro:  
    # Atributo de clase 
    alas = True
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie


mi_pajaro = Pajaro("Negro","Tucán")
print(mi_pajaro.color)
print(mi_pajaro.especie)
print(Pajaro.alas)


# ejercicio practica 1 

class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos


casa_blanca = Casa("blanca",4)

# ejercicio practica 2 

class Cubo: 
    caras = 6
    def __init__(self,color):
        self.color = color

cubo_rojo = Cubo("Rojo")


# ejercicio practica 3 

class Personaje:
    real = False
    def __init__(self,especie,magico,edad):
        self.especie =especie
        self.magico =magico
        self.edad = 17

harry_potter = Personaje ("Humano",True,17)