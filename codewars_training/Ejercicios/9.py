"""
Complete el método/función para que convierta las palabras delimitadas por guiones o guiones bajos
 a mayúsculas y minúsculas. La primera palabra del resultado debe escribirse en mayúsculas solo si
   la palabra original también lo estaba (lo que se conoce como mayúsculas y minúsculas, también
     conocido como mayúsculas Pascal). Las siguientes palabras siempre deben escribirse en 
     mayúsculas.

"""
string = 'a-cat-was-Hungry'



def to_camel_case(text):
    
    texto_nuevo=''
    palabras =[]
    texto_nuevo = text.replace('-',' ')
    texto_nuevo = texto_nuevo.replace('_',' ')
    palabras = texto_nuevo.split(' ')
    texto_nuevo=''
    for palabra in palabras: 
        texto_nuevo += palabra.capitalize()
    return(texto_nuevo)


print(to_camel_case(string))

    