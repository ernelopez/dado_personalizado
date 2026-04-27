import streamlit as st
import random

st.title("simulador de dado personalizado")

st.write("Ingresá el contenido de cada cara del dado:")

# Entradas del usuario
caras = []
for i in range(6):
    cara = st.text_input(f"Cara {i+1}", value="Piedra", key=f"cara_{i}")
    caras.append(cara)

# Botón para tirar
if st.button("Tirar"):
    if any(c.strip() == "" for c in caras):
        st.warning("Debés completar las 6 caras.")
    else:
        resultado = random.choice(caras)
        st.success(f"Resultado: {resultado}")
