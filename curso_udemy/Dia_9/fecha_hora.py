from datetime import datetime

mi_fecha = datetime(2025,5,15,22,10,15)

print(mi_fecha)

#practica 1 

import datetime

mi_fecha = datetime.date(1999,2,3)
datetime.date(1999,2,3)
print(mi_fecha)
#practica 2 

hoy = datetime.date.today()
print(hoy)


#practica 3 
minutos=datetime.datetime.now()

print(minutos.minute)