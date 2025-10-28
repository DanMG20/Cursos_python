import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

img = Image.open("sources/chilakas shorts.png")
# Para cambiar el nombre de la ventana y cambiar icono
st.set_page_config(page_title='Mi APP', page_icon='img', layout='wide')

def basicos_texto(): 
    # Titulo equivalente a un h1 literal
    st.title("Curso de Streamlit")
    # Header equivalente a h2 
    st.header("Que rollo bollo")
    # subheader equivalente a h3 
    st.subheader("Q culo")
    # texto
    st.text("Papaya de celaya")
    # Soporta markdown tbn
    st.markdown("## Esto es markdown")

    st.success("Exito")

    st.warning("advertencia")

    st.info("Información")

    st.error("Error")

    st.exception("k Paso ")


    st.write("Texto normal")

    st.write("### Tambien puede ir aqui texto markdown")


def cargar_archivo():
    st.header("DataFrame")
    dataframe = pd.read_csv('data/YT.csv')
    #Esto muestra el dataframe en la pagina 
    st.dataframe(dataframe)

    st.header("Dataframe de maximos")
    numeric_cols = dataframe.select_dtypes(include="number").columns
    st.dataframe(dataframe.style.highlight_max(subset=numeric_cols,axis=0))
    st.header("Muestra las primeras 5 filas de un data frame ")
    st.write(dataframe.head())
    st.json({"clave":"valor"})

    #Funcion para mostrar codigo 

    codigo = """ 
    def saludar(): 
        print("Hola")

    """

    st.code(codigo, language="python")

    #selectbox

    opcion = st.selectbox('Elije tu fruta favorita', ['CUKA','QLO'])


    #Multiselect 

    opciones = st.multiselect('Selecciona tus colores favoritos', ["Rosa ", "Blanco","Azul"])

    #sliders

    edad = st.slider( 
        'Selecciona tu edad',
        min_value=0,
        max_value=100,
        value=25,# Valor inicial
         step= 1
    )
    st.write('Tu edad es:', edad)

    #Imagens
    img = Image.open("sources/chilakas shorts.png")
    st.image(img, use_container_width=True)
    # Abrir video
    with open("sources/JAJAJA Avisenmeee.mp4","rb") as video_file:
        st.video(video_file.read(), start_time=0)
    # Abrir AUdio 

    with open("sources/TUMA.mp3", "rb") as video_file:
        st.video(video_file.read(), start_time=0)

def inputs(): 
    nombre= st.text_input("Ingresa tu nombre")
    st.title(nombre)

    mensaje = st.text_area("Ingresa tu mensaje", height=100)
    st.write(mensaje)

    numero = st.number_input('Ingresa un número', 1, 25)
    st.write(numero)

    
    fecha = st.date_input('Selecciona la fecha')
    st.write(fecha)

    hora = st.time_input('Selecciona la hora')
    st.write(hora)

    color = st.color_picker("selecciona un color")
    st.write(color)

def side_bar():
    st.sidebar.header('Navegacion')

if __name__ == '__main__': 
    inputs()
    side_bar()
    