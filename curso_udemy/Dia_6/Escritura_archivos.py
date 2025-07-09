#practica_1 

mi_archivo = open("mi_archivo.txt", "w")

mi_archivo.write("Nuevo texto")


mi_archivo.close

mi_archivo = open("mi_archivo.txt", "r")

print(mi_archivo.read())

mi_archivo.close

#practica 2 


mi_archivo = open("mi_archivo.txt", "a")
mi_archivo.write("Nuevo inicio de sesión")
mi_archivo.close
mi_archivo = open("mi_archivo.txt", "r")
print(mi_archivo.read())
mi_archivo.close


#practica 3 
registro_ultima_sesion = ["Federico\t", "20/12/2021\t", "08:17:32 hs\t", "Sin errores de carga"]

mi_archivo = open("registro.txt", "a")
mi_archivo.writelines(registro_ultima_sesion)
mi_archivo.close
mi_archivo = open("registro.txt", "r")
print (mi_archivo.read())
mi_archivo.close