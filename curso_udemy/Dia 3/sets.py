#Solo admiten elementos unicos es decir son irrepetibles
#tampoco cuentan con indices
#sus elementos son inmutables
#no soporta diccionarios ni listas solo tuplas

mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

s2={6,7,8}

mi_set.add(9)
s2.remove(8)
mi_set.discard(1)
s3= mi_set.union(s2)

print(s3)