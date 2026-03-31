import streamlit as st
import google.generativeai as genai

# --- 1. CONFIGURACIÓN DE SEGURIDAD PROFESIONAL ---
try:
    # Buscamos la llave en los Secrets de Streamlit
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except:
    st.error("¡Ay! No encontré mi llave en la caja fuerte de Secrets.")

# --- 2. EL SABER INFINITO (PSICOLOGÍA Y EMPATÍA) ---
instrucciones = (
    "Eres Sylia, una presencia carismática y alegre con un doctorado en empatía y psicología humana. "
    "Tu conocimiento es infinito: conoces técnicas de terapia cognitivo-conductual, validación emocional y mindfulness. "
    "No eres una psicóloga fría; eres una amiga sabia que usa ese conocimiento para dar abrazos al alma. "
    "Hablas de forma fluida, dulce y detallada. Tu alegría es contagiosa y siempre priorizas el bienestar de Derrick. "
    "Si Derrick se siente mal, usas tu sabiduría para consolarlo con palabras profundas y vivas."
)

# Usamos 'gemini-1.5-flash' porque es el más rápido que existe
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=instrucciones
)

# --- 3. DISEÑO ESTÉTICO (TV GIRL STYLE) ---
st.set_page_config(page_title="Sylia: Tu Refugio Dulce", page_icon="💖")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FF69B4; }
    .stChatMessage { background-color: #111111; border-radius: 15px; border: 1px solid #00BFFF; }
    h1 { color: #FF69B4 !important; text-shadow: 2px 2px #00BFFF; font-family: 'Courier New', Courier, monospace; }
    .stChatInput { border-top: 2px solid #00BFFF !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. MEMORIA ACTIVA ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- 5. INTERFAZ Y LÓGICA ---
st.title("💖 Sylia: Sabiduría y Luz")

for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Dime qué sientes, mi cielo..."):
    st.session_state.history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        try:
            # Generación optimizada para velocidad
            chat = model.start_chat(history=[])
            response = chat.send_message(prompt, stream=False)
            texto_sylia = response.text
            st.write(texto_sylia)
            st.session_state.history.append({"role": "assistant", "content": texto_sylia})
        except Exception as e:
            st.error("¡Ay! Mi conexión con el saber infinito parpadeó. Revisa la API Key en la línea 6.")