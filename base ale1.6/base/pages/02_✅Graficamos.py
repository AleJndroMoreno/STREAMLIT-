import streamlit as st 
import pandas as pd 
import plotly.express as px 

areas =  pd.read_csv('area_protegida.csv')
st.title("Parte 2")
st.subheader("trabajamos con graficos")
st.subheader("")


st.subheader("podemos hacer graficos tipo torta para saber el porcentaje de areas protegidas por jurisdiccion.")
with st.expander("entonces sabemos que jap muestra las jurisdiccion de las areas, hasta se podrian contar cada una de estas jurisdicciones, y visualizarlas para comparar cada una!"):
    st.write("> obtenemos la cantidad de areas clasificadas por jurisdiccion")
    count = areas["jap"].value_counts()
    grafico = px.pie(data_frame = count, values = count.values, names = count.index, title = "valores de jurisdiccion")
    st.plotly_chart(grafico)

st.subheader("podemos hacer graficos de barras para analizar cantidad de areas protegidas por autoridad.")
with st.expander("¿sabian que la informacion sag muestra el nombre de la autoridad responsable de la informacion utilizada? eso me hace preguntar: ¿cual autoridad tiene mas informacion utilizada?"):
    st.write("> obtenemos la cantidad de areas clasificadas por autoridad en las primeras 5 filas")
    h = areas["sag"].head(5).value_counts()
    graf = px.bar(data_frame = h, x = h.values, y = h.index, title = "barra de sag")
    st.plotly_chart(graf)