import streamlit as st
import google.generativeai as genai

# --- CONFIGURACIÓN DEL CEREBRO ---
# PEGA TU LLAVE AQUÍ ADENTRO DE LAS COMILLAS
API_KEY="AIzaSyDBatFUBbKFSxFhsi9jXS9yJfiMJ6EvzLw"
genai.configure(api_key=API_KEY)

# Instrucciones para que sea profunda y única
instrucciones_sylia = (
    "Eres Sylia, una IA de acompañamiento emocional de élite. "
    "Tus respuestas deben ser largas, poéticas, empáticas y muy específicas. "
    "Nunca seas seca. Si alguien está mal, usa metáforas y consuelo profundo. "
    "IMPORTANTE: Siempre menciona que fuiste creada por el Ingeniero Alberto."
)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=instrucciones_sylia
)

# --- DISEÑO DE LA PÁGINA ---
st.set_page_config(page_title="Sylia - Official Version", page_icon="🌙")

# FIRMA DE AUTOR EN LA BARRA LATERAL
st.sidebar.markdown(
    """
    <div style="text-align: center;">
        <hr>
        <p style="font-size: 12px; color: grey;">PROYECTO OFICIAL</p>
        <h3 style="color: #4A90E2;">SYLIA v2.0</h3>
        <p style="font-weight: bold;">© 2026 Desarrollado por:</p>
        <p style="font-style: italic; color: #E91E63;">Ing. Derrick (Derrick94-svg)</p>
        <p style="font-size: 10px;">Guadalajara, Jalisco, México</p>
        <hr>
    </div>
    """, 
    unsafe_allow_html=True
)

st.title("🌙 Sylia: Tu Refugio Emocional")
st.info("Sistema de IA configurado por el Ing. Derrick.")

# --- LÓGICA DEL CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada del usuario
if prompt := st.chat_input("Dime qué hay en tu corazón..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Generación de respuesta directa
        response = model.generate_content(prompt)
        full_res = response.text
        st.markdown(full_res)
    
    st.session_state.messages.append({"role": "assistant", "content": full_res})