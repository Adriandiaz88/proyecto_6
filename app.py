import pandas as pd
import plotly.express as px
import streamlit as st

#Encabezado de pagina
st.header('Graficas comparativas cantidad y precio contra kilometraje')

# leer los datos
car_data = pd.read_csv('vehicles_us.csv') 

# Esta es la linea para crear casilla de verificación para el histograma
show_hist = st.checkbox('Mostrar histograma')

# esta es la linea para crear casilla de verificación para el gráfico de dispersión
show_scatter = st.checkbox('Mostrar gráfico de dispersión')

# Para seleccionar la casilla para el histograma
if show_hist:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # Crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")
    # Mostrar el gráfico interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

# Para seleccionar la casilla para el gráfico de dispersión
if show_scatter:
    st.write('Creación de un gráfico de dispersión: precio vs. kilometraje')
    # Crear el gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Precio vs. Kilometraje")
    # Mostrar el gráfico interactivo
    st.plotly_chart(fig_scatter, use_container_width=True)