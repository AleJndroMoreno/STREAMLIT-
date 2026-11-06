import streamlit as st
import pandas as pd

# Cargar la base de datos
areas = pd.read_csv("area_protegida.csv")

st.title("Cuestionario sobre áreas protegidas")
st.write("Poné a prueba tus conocimientos sobre las areas protegidas.")

preguntas = [
    {
        "pregunta": "¿cual autoridad posee mas informacion sobre estas areas protegidas?",
        "opciones": ["MAyDS", "IGN"],
        "correcta": 1
    },
    {
        "pregunta": "¿cual calificacion de estas areas protegidas posee informacion sobre parques?",
        "opciones": ["tipo de area", "jurisdiccion"],
        "correcta": 0
    },
    {
        "pregunta": "¿en areas de jurisdiccion, cual tipo de area es la que posee mas informacion?",
        "opciones": ["nacional", "provincial", "municipal", "privado"],
        "correcta": 1
    },
]

for i, p in enumerate(preguntas):
    st.subheader(f"• Pregunta {i + 1} •")
    st.write(p["pregunta"])

    # El radio guarda la elección del estudiante
    eleccion = st.radio(
        "Elegí una opción:",
        p["opciones"],
        key=f"pregunta_{i}",
        index=None,
    )

    # Cada pregunta tiene su propio botón
    if st.button("Verificar", key=f"btn_{i}"):
        if eleccion is None:
            st.warning("⚠️ Elegí una opción antes de verificar.")
        elif eleccion == p["opciones"][p["correcta"]]:
            st.balloons()
            st.success("CACHING!!!! correcto.")
        else:
            correcta = p["opciones"][p["correcta"]]
            st.error(f"INCORRECTO DEDICATE MAS TIEMPO")

    st.divider()
    st.header("")