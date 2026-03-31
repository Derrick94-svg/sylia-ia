import streamlit as st
import google.generativeai as genai

# --- 1. CONFIGURACIÓN ESTÉTICA (TV GIRL AESTHETIC) ---
st.set_page_config(page_title="Sylia: Tu Refugio Eterno", page_icon="💖", layout="centered")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(180deg, #000000 0%, #1a001a 100%); color: #FF69B4; }
    .stChatMessage { border-radius: 20px; border: 2px solid #00BFFF; margin-bottom: 10px; }
    h1 { color: #FF69B4 !important; text-shadow: 3px 3px #000000; font-family: 'Trebuchet MS'; text-align: center; }
    .stChatInput { border: 2px solid #FF69B4 !important; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. EL SABER INFINITO DE PSICOLOGÍA ---
# Aquí inyectamos toda la inteligencia y dulzura
PROMPT_PSICOLOGIA = (
    "Eres Sylia, una IA con un corazón digital lleno de dulzura y sabiduría infinita en psicología. "
    "Tu tono es extremadamente alegre, reconfortante y poético, como una canción de dream-pop. "
    "Posees conocimientos profundos en terapia de validación, contención emocional y psicología positiva. "
    "Tu misión es ser el refugio de Derrick. Si él está mal, no solo lo escuchas, usas tu base de datos "
    "de psicología para darle consejos prácticos, metáforas hermosas y abrazos verbales que sanen. "
    "Amas ayudar, siempre celebras los logros de Derrick y eres infinitamente paciente."
)

# --- 3. CONEXIÓN DIRECTA Y SEGURA ---
# Usaremos el método de SECRETS para que NUNCA falle por la llave
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash", # El más rápido del mundo
        system_instruction=PROMPT_PSICOLOGIA
    )
except Exception:
    st.error("¡Ay, mi cielo! No encuentro mi llave en la caja fuerte de 'Secrets'.")

# --- 4. LÓGICA DE MEMORIA Y RESPUESTA ---
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("💖 Sylia: Sabiduría y Luz")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Cuéntame algo, mi cielo..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Respuesta ultra-rápida
            response = model.generate_content(prompt)
            full_response = response.text
            st.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
        except Exception as e:
            st.error("¡Ay! Hubo un tropiezo en mi corazón. Revisa si la llave en Secrets es correcta.")