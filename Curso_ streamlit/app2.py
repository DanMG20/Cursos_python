import streamlit as st
import pandas as pd
import plotly.express as px 


def main(): 

    st.header("DataFrame")
    dataframe = pd.read_csv('data/YT.csv')
    #Esto muestra el dataframe en la pagina 
    st.dataframe(dataframe)
    df_count = dataframe.groupby('Duration').count().reset_index()
    
    grafica_pastel = px.pie(df_count, values='Video title',names='Duration', title='Duración')
    st.plotly_chart(grafica_pastel) 


    df_average = dataframe.groupby('Video title')['Views'].mean().reset_index()
    fig2 = px.bar(df_average, x='Video title', y='Views')
    st.plotly_chart(fig2)
if __name__ == '__main__': 
    main()