import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Panel de análisis de anuncios de vehículos')

# Botón para histograma
if st.button('Mostrar histograma del odómetro'):
    st.write('Histograma de la columna "odometer"')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
if st.button('Mostrar gráfico de dispersión entre odómetro y precio'):
    st.write('Gráfico de dispersión entre "odometer" y "price"')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True)
