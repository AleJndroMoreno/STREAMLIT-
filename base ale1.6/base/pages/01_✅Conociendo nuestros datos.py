import pandas as pd
import streamlit as st

areas =  pd.read_csv('area_protegida.csv')
st.title("Parte 1")
st.header("veremos los datos mas frecuentes de areas protegidas y ejemplos de como podemos utilizarlos.")
st.subheader("")


st.subheader("jurisdiccion y tipo de area nos muestran informacion de las areas protegidas. Jurisdiccion nos muestra la autoridad de un area, y Tipo de area nos muestra el detalles de la area especifica.")
with st.expander("¿Cuántos numeros de filas y columnas tiene jurisdiccion en columna nacional y tipo de area en columna parque?"):
    c1 = areas[(areas["jap"] == 2)&(areas["tap"] == 1)].shape[0]
    st.write("area tiene dos secciones, jurisdiccion (JAP) y tipo de area (TAP)")
    st.write("> nacional se encuentra en jurisdiccion numero 2")
    st.write("> parque se encuentra en tipo de area numero 1")
    st.write("resultado: ", c1)
    

st.subheader("podemos acceder a la ubicacion de un area medienta sus longitudes y latitudes.")
with st.expander("¿como podemos acceder a la ubicacion de una area por su clasificacion y ubicacion?"):   
    g = areas[areas["tap"] == 3]
    cal = [g["lat"].mean(), g["lng"].mean()]
    st.write("clasificacion de area: monumento nacional")
    st.write("hacemos filtro de:")
    st.write("> lat (latencia)")
    st.write("> lng (longitud)")
    st.write("ubicacion de tipo de area monumento nacional: ", cal)

st.subheader("gna muestra parte del nombre geografico de las areas protegidas, nos da la oportunidad de buscar las que necesitamos y identificarlas")
with st.expander("intentemos buscar el nombre de un area protegida."):
    nomb = areas[areas["gna"] == "Parque Natural Municipal"]
    st.write("> Buscamos en gna: Parque Natural Municipal")
    st.write("de resultado, nos muestra todos los datos relacionados de \"Parque Natural Municipal\" ")
    st.write(nomb)
