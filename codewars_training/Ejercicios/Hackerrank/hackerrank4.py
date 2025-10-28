import math


s = "aba"
n = 10
def repeatedString(s, n):
    a_in_s  = s.count("a")
    repeticiones_completas = math.floor(n/len(s)) 
    remanente = n % len(s)
    as_en_remanente = 0 
    indice = 0
    for letra in s: 
        if indice<remanente: 
            indice+=1
            if letra =="a":
                as_en_remanente +=1
    
    total_as = a_in_s*repeticiones_completas + as_en_remanente
    return total_as

print(repeatedString(s,n))


