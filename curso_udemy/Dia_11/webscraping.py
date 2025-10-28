"""
html estructura y contenido 
css color y estilo 
javascript elementos interactivos 
"""

import bs4
import requests 

resultado = requests.get("https://escueladirecta.com/l/products?sortKey=name&sortDirection=asc&page=1")

sopa = bs4.BeautifulSoup(resultado.text,'lxml')

imagenes = sopa.select('.course-box-image')

for i in imagenes:
    print(imagenes)