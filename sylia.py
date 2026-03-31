import streamlit as st
import google.generativeai as genai

# CONFIGURACIÓN BÁSICA
# Pon aquí tu llave NUEVA de Google AI Studio
API_KEY = "AIzaSyDBatFUBbKFSxFhsi9jXS9yJfiMJ6EvzLw"
genai.configure(api_key=API_KEY)

st.title("Prueba de Conexión - Ing. Derrick")

# El modelo más simple posible
model = genai.GenerativeModel("gemini-1.5-flash")

if prompt := st.chat_input("Dime hola para probar..."):
    st.chat_message("user").markdown(prompt)
    try:
        response = model.generate_content(prompt)
        st.chat_message("assistant").markdown(response.text)
    except Exception as e:
        st.error(f"Error técnico: {e}")