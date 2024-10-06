import streamlit as st

# Título de la aplicación
st.title("Conectando a adultos mayores 🤝")

# Input para ingresar el nombre del adulto mayor
nombre = st.text_input("Ingresa tu nombre:")

# Opciones de grupos de interés y actividades comunitarias
grupos_interes = {
    "Artes y manualidades": ["Pintura", "Bordado", "Tejido"],
    "Deportes y ejercicio": ["Yoga", "Caminar", "Tai Chi"],
    "Aprendizaje y tecnología": ["Clases de idiomas", "Programación", "Gadgets"],
    "Voluntariado y servicio": ["Cuidado de animales", "Asistencia en eventos comunitarios", "Donaciones"],
}

intereses_seleccionados = st.multiselect("Selecciona tus intereses y actividades:", list(grupos_interes.keys()))
actividades_seleccionadas = []

for interes in intereses_seleccionados:
    actividades_seleccionadas.extend(grupos_interes[interes])

# Mostrar actividades seleccionadas
if actividades_seleccionadas:
    st.write(f"Tus actividades seleccionadas son: {', '.join(actividades_seleccionadas)}")
else:
    st.write("Por favor, selecciona al menos un interés o actividad.")

# Chat para comunicarse con familia y amigos
st.subheader("Chatea con tu familia y amigos 💬")
mensajes = st.chat_history()

mensaje_nuevo = st.text_input("Escribe tu mensaje:", key="mensaje_nuevo")

if st.button("Enviar", key="enviar_mensaje"):
    mensajes.append((nombre, mensaje_nuevo))
