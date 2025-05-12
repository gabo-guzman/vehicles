import streamlit as st
import pandas as pd
import plotly.express as px


car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
price_for_cylinders = car_data.pivot_table(
    index="cylinders", values="price", aggfunc="mean").reset_index()
price_for_cylinders["price"] = price_for_cylinders["price"].round()
price_for_type = car_data.pivot_table(index="type", values="price", aggfunc="mean").reset_index(
).sort_values(by="price", ascending=False)
st.header("¿Qué relación tiene el número de cilindros con el precio del vehículo")
hist_button = st.button(' cilindros vs precio')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('generando...')

# crear un histograma
    fig = px.bar(price_for_cylinders, x="cylinders", y="price")

# mostrar un gráfico Plotly interactivo
st.plotly_chart(fig, use_container_width=True)

st.header("¿Afecta el tipo al precio del vehículo")
hist_button = st.button('tipo vs precio')  # crear un botón


if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('generando...')

# crear un histograma
    fig = px.bar(price_for_type, x="type", y="price")


# mostrar un gráfico Plotly interactivo
st.plotly_chart(fig, use_container_width=True)
