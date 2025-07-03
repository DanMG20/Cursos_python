nombre = input("porfavor ingresa tu nombre:  ")
ventas = input("Ingresa el total de ventas mamasita: ")
comision = round(float(ventas)/100*13,2)

print(f"Hola {nombre}, tu comisión sería de ${comision}")
