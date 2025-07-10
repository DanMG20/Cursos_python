class Animal: 
    def __init__(self,edad ,color):
        self.edad = edad
        self.color =color
    def nacer (self):
        print("Este animal a nacido")

    def hablar(self):
        print( "Este animal emite un sonido")



class Pajaro(Animal):

    def __init__ (self, edad, color , altura_vuelo):
        # el metodo super hereda todas las variables de la clase Padre
        super.__init__(edad,color)
        self.altura_vuelo = altura_vuelo
    def hablar(self): 
        print("pio")

    def volar(self, metros): 
        print(f"El pajaro vuela {metros} metros")
piolin = Pajaro(4,"Blanco",50)

piolin.volar(100)

print(piolin.color)
print(piolin.edad)


# Practica 1 

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad



class Alumno(Persona): 
    pass



# Practica 2

class Mascota: 
    def __init__(self,edad,nombre,cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas



class Perro(Mascota):
    pass


#practica 3

class Vehiculo: 
    def acelerar(self):
        pass
    def frenar(self):
        pass


class Automovil(Vehiculo):
    pass


class Padre: 
     def hablar(self):
        print ("Hola")


class Madre: 
    def reir(self):
        print ("Ja ja")

    def hablar():
        print("que tranza papi")
class Hijo (Padre,Madre):
    pass

class Nieto(Hijo): 
    pass



mi_nieto =Nieto ()

mi_nieto.hablar()
mi_nieto.reir()

#Practica 3 

class Padre:
    def __init__(elf,color_ojos,tipo_pelo,altura,voz,deporte_preferido):
        pass
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"
    def reir(self):
        return "Jajaja"
    def hobby(self):
        return "Pinto madera en mi tiempo libre"
    def caminar(self):
        return "Caminando con pasos largos y rápidos"
        
class Hijo(Padre):
    pass
    