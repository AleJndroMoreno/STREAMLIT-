import pandas as pd 
import streamlit as st 
import plotly.express as px 

areas =  pd.read_csv('area_protegida.csv')
st.title("Parte 1")
st.header("sabemos que jurisdiccion y tipo de area nos muestran informacion de las areas protegidas. Jurisdiccion nos muestra la autoridad de un area, y Tipo de area nos muestra el detalles de la area especifica.")

with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    c1 = areas[(areas["jap"] == 2)&(areas["tap"] == 1)].shape[0]
    st.write(c1)

    
st.title("Parte 2")
with st.expander("podemos saber la ubicacion de una areas protegidas por esta columna Area he incluso podemos buscar informacion mas precisa."):
    g = areas[areas["area"] >= 20000000]
    st.write(g)


st.title("Parte 3")
with st.expander("entonces sabemos que jap muestra las jurisdiccion de las areas, hasta se podrian contar cada una de estas jurisdicciones, y visualizarlas para comparar cada una!"):
    count = areas["jap"].value_counts()
    grafico = px.pie(data_frame = count, values = count.values, names = count.index, title = "valores de juri")
    
    st.plotly_chart(grafico)