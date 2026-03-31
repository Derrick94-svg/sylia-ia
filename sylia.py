import streamlit as st
import google.generativeai as genai

# --- CONFIGURACIÓN DE LA IA ---
# Aquí pegaremos tu llave secreta en el siguiente paso
API_KEY = AIzaSyCs3rqlkhkHI3AY1ZmS-wG_3CA7yFsEGhQ
genai.configure(api_key=API_KEY)

# Configuración del modelo para que sea empático y profundo
generation_config = {
  "temperature": 0.7,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 1000,
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="Eres Sylia, una asistente de acompañamiento emocional profesional, dulce y profunda. Tu objetivo es escuchar, validar sentimientos y ofrecer reflexiones largas y reconfortantes. Si detectas peligro de suicidio, ofrece siempre la Línea de la Vida 800 911 2000."
)

# --- INTERFAZ DE STREAMLIT ---
st.set_page_config(page_title="Sylia - IA Emocional", page_icon="🌙")
st.title("🌙 Conoce a Sylia")
st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada del usuario
if prompt := st.chat_input("Cuéntale tus pensamientos a Sylia..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # La IA genera la respuesta aquí
        chat = model.start_chat(history=[
            {"role": m["role"] if m["role"] == "user" else "model", "parts": [m["content"]]} 
            for m in st.session_state.messages[:-1]
        ])
        
        response = chat.send_message(prompt)
        full_response = response.text
        st.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})