import streamlit as st

# Inicializar el estado de la sesión para almacenar mensajes y mensaje_nuevo
if 'mensajes' not in st.session_state:
    st.session_state['mensajes'] = []
if 'mensaje_nuevo' not in st.session_state:
    st.session_state['mensaje_nuevo'] = ""

# Título de la aplicación
st.title("Conectando a Adultos Mayores 🤝")

# Entrada para el nombre del adulto mayor
nombre = st.text_input("Ingresa tu nombre:")

# Opciones de grupos de interés y actividades comunitarias
grupos_interes = {
    "Artes y Manualidades": ["Pintura", "Bordado", "Tejido"],
    "Deportes y Ejercicio": ["Yoga", "Caminar", "Tai Chi"],
    "Aprendizaje y Tecnología": ["Clases de Idiomas", "Programación", "Gadgets"],
    "Voluntariado y Servicio": ["Cuidado de Animales", "Asistencia en Eventos Comunitarios", "Donaciones"],
}

st.header("Selecciona tus intereses y actividades")

# Selección de grupos de interés
intereses_seleccionados = st.multiselect(
    "Elige tus intereses:",
    options=list(grupos_interes.keys())
)

# Selección de actividades basadas en los intereses seleccionados
actividades_seleccionadas = []
for interes in intereses_seleccionados:
    actividades = st.multiselect(
        f"Selecciona actividades en **{interes}**:",
        options=grupos_interes[interes],
        key=f"actividad_{interes}"  # Clave única para cada multiselect
    )
    actividades_seleccionadas.extend(actividades)

# Mostrar actividades seleccionadas
if actividades_seleccionadas:
    st.success(f"Tus actividades seleccionadas son: {', '.join(actividades_seleccionadas)}")
else:
    st.warning("Por favor, selecciona al menos una actividad.")

# Separador
st.markdown("---")

# Subtítulo para el chat
st.header("Chatea con tu Familia y Amigos 💬")

# Mostrar historial de mensajes
for msg in st.session_state['mensajes']:
    st.write(f"**{msg['nombre']}**: {msg['mensaje']}")

# Entrada para un nuevo mensaje
mensaje_nuevo = st.text_input("Escribe tu mensaje:", key="mensaje_nuevo")

# Botón para enviar el mensaje
if st.button("Enviar", key="enviar_mensaje"):
    if nombre.strip() == "":
        st.error("Por favor, ingresa tu nombre antes de enviar un mensaje.")
    elif mensaje_nuevo.strip() == "":
        st.error("El mensaje no puede estar vacío.")
    else:
        st.session_state['mensajes'].append({"nombre": nombre, "mensaje": mensaje_nuevo})
        st.success("Mensaje enviado!")
        # Limpiar el campo de texto después de enviar
        st.session_state['mensaje_nuevo'] = ""
