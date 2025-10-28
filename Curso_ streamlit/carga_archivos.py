import streamlit as st 
from PIL import Image 
import pandas as pd
import docx2txt
from PyPDF2 import PdfReader
import os
# Permite almacenar en cache la imagen (ahorra tiempo de proceso ya que se precarga en cache)
@st.cache_data
def cargar_imagen(image_file): 
    img = Image.open(image_file)
    return img

def leer_pdf(pdf_file):
    pdfReader= PdfReader(pdf_file)
    count = len(pdfReader.pages)
    todo_el_texto = ''
    for i in range(count):
        pagina = pdfReader.pages[i]
        todo_el_texto +=pagina.extract_text()
    return todo_el_texto

def guardar_archivo(file): 
    if  not os.path.exists('temp'): 
        os.makedirs('temp')

    with open(os.path.join('temp', file.name), 'wb') as f:
        f.write(file.getbuffer())
        return st.success(f'Archivo guardado: {file.name} en temp')
    

    
def main(): 
    st.title('Tutorial de carga de archivos')
    menu = ['Imagenes', 'Conjunto de datos', 'Archivos de Documentos']
    eleccion = st.sidebar.selectbox('Menu', menu)

    if eleccion== 'Imagenes': 
        st.subheader('Imagen')

        archivo_imagen = st.file_uploader('Subir Imagenes', type =['png', 'jpg','jpeg'])
        if archivo_imagen is not None: 
            detalles_archivo={ 'nombre_archivo': archivo_imagen.name,
                             'tipo_archivo': archivo_imagen.type,
                             'tamaño_archivo': archivo_imagen.size}
            st.write(detalles_archivo)
            st.image(cargar_imagen(archivo_imagen), width=250)
            guardar_archivo(archivo_imagen)  

    elif eleccion == 'Conjunto de datos':
        st.subheader('Conjunto de datos')
        archivo_datos = st.file_uploader('Subir Imagenes', type =['csv', 'xlsx'])
        if archivo_datos is not None:
              detalles_archivo={ 'nombre_archivo': archivo_datos.name,
                             'tipo_archivo': archivo_datos.type,
                             'tamaño_archivo': archivo_datos.size}
              st.write(detalles_archivo)
              

        if detalles_archivo['tipo_archivo'] == 'text/csv':
            df = pd.read_csv(archivo_datos)
        elif detalles_archivo['tipo_archivo'] =="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            df = pd.read_excel(archivo_datos)

            st.dataframe(df)
        else:
            df =  pd.DataFrame()
            st.dataframe(df)

        guardar_archivo(archivo_datos)

    elif eleccion == 'Archivos de Documentos': 
        st.subheader('Docs')
        archivo_doc = st.file_uploader('Subir documento', type =['pdf', 'txt','docx'])
        if st.button('Procesar'):
            if archivo_doc is not None: 
                detalles_archivo={ 'nombre_archivo': archivo_doc.name,
                                'tipo_archivo': archivo_doc.type,
                                'tamaño_archivo': archivo_doc.size}
                st.write(detalles_archivo)
                if archivo_doc.type == "application/pdf":
                    texto = leer_pdf(archivo_doc)
                    st.write(texto)

                elif archivo_doc.type == "text/plain":
                    texto = str(archivo_doc.read(), "utf-8")
                    st.write(texto)

                guardar_archivo(archivo_doc)
                #elif archivo_doc.type ==""



if __name__ == "__main__": 
    main()
    