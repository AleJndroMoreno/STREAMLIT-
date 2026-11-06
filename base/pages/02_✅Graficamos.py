import streamlit as st 
import pandas as pd 
import plotly.express as px 

areas =  pd.read_csv('area_protegida.csv')
st.title("trabajamos con graficos")
with st.expander("entonces sabemos que jap muestra las jurisdiccion de las areas, hasta se podrian contar cada una de estas jurisdicciones, y visualizarlas para comparar cada una!"):
    count = areas["jap"].value_counts()
    grafico = px.pie(data_frame = count, values = count.values, names = count.index, title = "valores de juri")
    st.plotly_chart(grafico)

with st.expander("¿sabian que la informacion sag muestra el nombre de la autoridad responsable de la informacion utilizada? eso me hace preguntar: ¿cual autoridad tiene mas informacion utilizada?"):
    h = areas["sag"].head(5).value_counts()
    graf = px.bar(data_frame = h, x = h.values, y = h.index, title = "barra de sag")
    st.plotly_chart(graf)