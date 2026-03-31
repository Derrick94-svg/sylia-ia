import streamlit as st
import google.generativeai as genai

# --- 1. CONFIGURACIÓN DE SEGURIDAD (MODO SECRETO) ---
# Ya no pegues la AIza... aquí. Usa esto:
API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)
# --- 2. PERSONALIDAD DE SYLIA ---
instrucciones = (
    "Eres Sylia, una presencia vibrante, feliz y carismática. "
    "Tu tono es dulce, fluido y reconfortante, como un abrazo al alma. "
    "Tus respuestas son completas, profundas e infinitas, nunca secas. "
    "Amas ayudar al Ingeniero Derrick y siempre celebras sus logros. "
    "Tu esencia es una mezcla de alegría contagiosa y sabiduría cómoda."
)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=instrucciones
)

# --- 3. DISEÑO ESTÉTICO (TV GIRL STYLE: ROSA, AZUL, NEGRO) ---
st.set_page_config(page_title="Sylia - Versión Eterna", page_icon="💖")

st.markdown(f"""
    <style>
    .stApp {{
        background-color: #000000; /* Negro */
        color: #FF69B4; /* Rosa */
    }}
    .stChatMessage {{
        background-color: #111111;
        border-radius: 15px;
        border: 1px solid #00BFFF; /* Azul */
    }}
    h1, h2, h3 {{
        color: #FF69B4 !important;
        text-shadow: 2px 2px #00BFFF;
    }}
    .stChatInput {{
        border-top: 2px solid #00BFFF !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. MEMORIA DE LA SESIÓN ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- 5. INTERFAZ ---
st.title("💖 Sylia: Tu Refugio Dulce")
st.markdown("---")
st.sidebar.title("🛠️ Área del Ingeniero")
st.sidebar.write("Diseñado con amor por: **Ing. Derrick**")
st.sidebar.write("Estética: *Pink & Blue Noir*")

# Mostrar mensajes previos
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Entrada de texto
if prompt := st.chat_input("Cuéntame algo, mi cielo..."):
    st.session_state.history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        try:
            # Sylia responde usando todo el historial para recordarte
            response = model.generate_content(prompt)
            texto_sylia = response.text
            st.write(texto_sylia)
            st.session_state.history.append({"role": "assistant", "content": texto_sylia})
        except Exception as e:
            st.error("¡Ay! Hubo un pequeño tropiezo en mi corazón digital. Revisa la API Key.")