import pandas as pd
import streamlit as st

areas =  pd.read_csv('area_protegida.csv')
st.title("Parte 1")
st.header("sabemos que jurisdiccion y tipo de area nos muestran informacion de las areas protegidas. Jurisdiccion nos muestra la autoridad de un area, y Tipo de area nos muestra el detalles de la area especifica.")

with st.expander("¿Cuántas filas y columnas tiene jurisdiccion en columna nacional y tipo de area en columna parque?"):
    c1 = areas[(areas["jap"] == 2)&(areas["tap"] == 1)].shape[0]
    st.write(c1)
    


with st.expander("podemos saber la ubicacion de una areas protegidas por esta columna Area he incluso podemos buscar informacion mas precisa."):   
    g = areas[areas["area"] >= 20000000]
    g["area"]
    st.write(g)

with st.expander("¿sabian que gna muestra parte del nombre geografico de las areas protegidas? nos da la oportunidad de buscar las que necesitamos y identificarlas"):
    nomb = areas[areas["gna"] == "Parque Natural Municipal"]
    st.write(nomb)
