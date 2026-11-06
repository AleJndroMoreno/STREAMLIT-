import folium as folk
from streamlit_folium import folium_static
import streamlit as st
import pandas as pd 

areas =  pd.read_csv('area_protegida.csv')

st.title("utilizamos mapas geograficos")

with st.expander("al importar folium, podriamos navegar en un mapa lo que nosotros le mandamos a los comandos a hacer. seria interesante saber donde se ubican los lugares privados de jurisdiccion."):
    g = areas[areas["jap"] == 5]

    mapa = folk.Map(
        location=[g["lat"].mean(), g["lng"].mean()],
        zoom_start=4
    )

    for _, fila in g.iterrows():

        folk.CircleMarker(
            location=[fila["lat"], fila["lng"]],
            radius=6,
          #  color=colors.get(fila["jap"], "cyan"),
            popup=fila["nam"]
        ).add_to(mapa)
    
    folium_static(mapa, width=700, height=500)