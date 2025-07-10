class Vaca: 
    def __init__(self,nombre):
        self.nombre = nombre 


    def hablar (self):
        print(self.nombre + " dice muu")

    

class Oveja: 
    def __init__(self,nombre):
        self.nombre = nombre 


    def hablar (self):
        print(self.nombre + " dice bee")


vaca1 = Vaca("Aurora")
oveja1 = Oveja("Nube")


animales =[vaca1,oveja1]

for animal in animales:
    animal.hablar()



def animal_habla(animal): 
    animal.hablar()



animal_habla(vaca1)
animal_habla(oveja1)


#Practica 1

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

iterar = [palabra,lista,tupla]

for iteracion in iterar: 
    print(len(iteracion))


#Practica 2 
class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")


arquero1 =Arquero()
mago1= Mago()
samurai1=Samurai() 

personajes = [arquero1,mago1,samurai1]

for personaje in personajes: 
    personaje.atacar()


#Practica 3

class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

def personaje_defender(objeto):
    objeto.defender()


