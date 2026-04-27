import streamlit as st
import random

st.title("simulador de dado personalizado")

st.write("Ingresá el contenido de cada cara del dado:")

# Entradas del usuario
caras = []
for i in range(6):
    cara = st.text_input(f"Cara {i+1}", key=f"cara_{i}")
    caras.append(cara)

# Botón para tirar
if st.button("Tirar"):
    # Filtrar caras no vacías
    caras_validas = [c for c in caras if c.strip() != ""]
    
    if len(caras_validas) == 0:
        st.warning("Ingresá al menos una cara válida.")
    else:
        resultado = random.choice(caras_validas)
        st.success(f"Resultado: {resultado}")