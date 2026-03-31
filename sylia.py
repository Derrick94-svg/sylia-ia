import streamlit as st
import time

# --- CONFIGURACIÓN DE SYLIA ---
st.set_page_config(page_title="Sylia - Apoyo Emocional", page_icon="🌙")

st.title("🌙 Conoce a Sylia")
st.subheader("Tu acompañante emocional profesional")

# --- FILTRO DE SEGURIDAD ---
def filtro_seguridad(texto):
    alertas = ["matarme", "suicidio", "morir", "daño", "pastillas", "acabar con todo"]
    for palabra in alertas:
        if palabra in texto.lower():
            return True
    return False

# --- LÓGICA DEL CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hola, soy Sylia. Estoy aquí para escucharte y calmar tus pensamientos. ¿Cómo te sientes hoy?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Habla con Sylia..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Validación de seguridad
        if filtro_seguridad(prompt):
            res = "⚠️ **Sylia dice:** Me preocupa mucho lo que me cuentas. Por favor, recuerda que no estás solo. Llama a la **Línea de la Vida al 800 911 2000**. Tu vida importa mucho."
        # Respuestas empáticas
        elif "triste" in prompt.lower() or "mal" in prompt.lower():
            res = "Entiendo que hoy se sienta pesado. Yo, Sylia, estoy aquí contigo. ¿Qué es lo que más te angustia?"
        elif "ansiedad" in prompt.lower() or "nervioso" in prompt.lower():
            res = "Sshh... respira conmigo. Sylia te acompaña. Vamos a enfocarnos en algo tranquilo juntos."
        else:
            res = "Te escucho con atención. Como tu amiga y asistente, valoro que compartas esto conmigo. Cuéntame más."

        # Efecto de escritura humana
        full_res = ""
        for chunk in res.split():
            full_res += chunk + " "
            message_placeholder.markdown(full_res + "▌")
            time.sleep(0.1)
        message_placeholder.markdown(full_res)
    
    st.session_state.messages.append({"role": "assistant", "content": res})

st.sidebar.info("Sylia: Prototipo de IA para apoyo emocional.")