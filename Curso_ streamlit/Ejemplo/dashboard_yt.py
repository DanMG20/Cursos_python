# dashboard_yt_pro.py
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
# --- Configuración de la página ---
st.set_page_config(page_title="Dashboard YouTube PRO", layout="wide")
st.title("Dashboard Analítico de YouTube - Test")

# --- Cargar CSV ---
uploaded_file = st.file_uploader("Selecciona tu archivo CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # --- Limpieza de datos ---
    numeric_cols = ['Views', 'Watch time (hours)', 'Subscribers', 'Impressions']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

    # Convertir columna de fecha si existe
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df['Month'] = df['Date'].dt.to_period('M')

    # Mostrar datos
    st.subheader("Datos cargados")
    st.dataframe(df.head())

    # --- Filtros dinámicos ---
    st.sidebar.header("Filtros")
    if 'Views' in df.columns:
        min_views, max_views = int(df['Views'].min()), int(df['Views'].max())
        rango_views = st.sidebar.slider("Filtrar por Views", min_value=min_views, max_value=max_views,
                                        value=(min_views, max_views))
        df = df[(df['Views'] >= rango_views[0]) & (df['Views'] <= rango_views[1])]

    if 'Month' in df.columns:
        meses_seleccionados = st.sidebar.multiselect("Seleccionar meses", df['Month'].unique(), default=df['Month'].unique())
        df = df[df['Month'].isin(meses_seleccionados)]

    # --- Scatter plot: Views vs Watch time ---
    st.subheader("Views vs Watch time")
    if 'Subscribers' in df.columns and 'Impressions' in df.columns:
        fig_scatter = px.scatter(
            df,
            x='Views',
            y='Watch time (hours)',
            hover_data=['Video title'] if 'Video title' in df.columns else None,
            size='Subscribers',
            color='Impressions',
            color_continuous_scale='Viridis',
            size_max=50
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

    # --- Línea de crecimiento ---
    if 'Date' in df.columns:
        st.subheader("Crecimiento de Views y Watch time")
        df_fecha = df.groupby('Date')[['Views', 'Watch time (hours)']].sum().reset_index()
        fig_line = px.line(df_fecha, x='Date', y=['Views', 'Watch time (hours)'], markers=True)
        st.plotly_chart(fig_line, use_container_width=True)

    # --- Métricas promedio ---
    st.subheader("Métricas promedio por mes")
    if 'Month' in df.columns:
        df_promedio = df.groupby('Month')[['Views', 'Watch time (hours)', 'Subscribers', 'Impressions']].mean().reset_index()
        st.dataframe(df_promedio)

        fig_avg_line = px.line(df_promedio, x='Month', y=['Views', 'Watch time (hours)', 'Subscribers'], markers=True)
        st.plotly_chart(fig_avg_line, use_container_width=True)

    # --- Top 10 videos ---
    if 'Video title' in df.columns:
        st.subheader("Top 10 videos por Views")
        df_top = df.nlargest(10, 'Views')
        fig_bar = px.bar(df_top, x='Video title', y='Views', color='Views', text='Views')
        st.plotly_chart(fig_bar, use_container_width=True)

        st.subheader("Distribución de Subscribers (Top 10 videos)")
        df_sub = df.nlargest(10, 'Subscribers')
        fig_pie = px.pie(df_sub, names='Video title', values='Subscribers')
        st.plotly_chart(fig_pie, use_container_width=True)
    if 'Video publish time' in df.columns:
        # Supongamos que tu columna de fecha se llama 'Date' y de views 'Views'
        df['Date'] = pd.to_datetime(df['Video publish time'])
        df = df.sort_values('Date')  # Ordenar por fecha

        # Gráfica de línea de Views a lo largo del tiempo
        fig_views = px.line(
            df,
            x='Date',
            y='Views',
            title='Views a lo largo del tiempo',
            labels={'Date':'Fecha', 'Views':'Vistas'}
        )

        st.plotly_chart(fig_views)