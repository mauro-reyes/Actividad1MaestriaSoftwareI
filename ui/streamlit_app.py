import streamlit as st

from ui.diagramas_view import mostrar_diagramas
from builder.automovil_builder import AutomovilBuilderConcreto
from bridge.plataforma import Web, Movil
from bridge.notificacion import AlertaCritica, MensajeInformativo
from mediator.sala_chat import SalaChat
from mediator.usuario import Usuario


def run_app():
    st.set_page_config(
        page_title="Laboratorio de Arquitectura de Software",
        layout="wide"
    )

    st.title("🛠️ Demostración de Patrones de Diseño")

    opcion = st.sidebar.radio(
        "Seleccione un módulo:",
        [
            "Builder – Automóviles",
            "Bridge – Notificaciones",
            "Mediator – Chat",
            "Diagramas C4"
        ]
    )

    # --- BUILDER ---
    if opcion == "Builder – Automóviles":
        st.header("Configurador de Automóvil")
        motor = st.selectbox("Motor", ["V6", "V8", "Eléctrico"])
        color = st.color_picker("Color", "#FFFFFF")
        llantas = st.selectbox("Llantas", ["R17", "R18", "R19"])
        gps = st.checkbox("GPS")
        techo = st.checkbox("Techo solar")

        builder = (
            AutomovilBuilderConcreto()
            .set_motor(motor)
            .set_color(color)
            .set_llantas(llantas)
            .set_gps(gps)
            .set_techo(techo)
        )

        auto = builder.build()
        st.json(vars(auto))

    # --- BRIDGE ---
    elif opcion == "Bridge – Notificaciones":
        st.header("Sistema de Notificaciones")

        mensaje = st.text_input("Mensaje", "Alerta del sistema")
        tipo = st.radio("Tipo", ["Crítica", "Informativa"])
        plataforma = st.radio("Plataforma", ["Web", "Móvil"])

        plataforma_obj = Web() if plataforma == "Web" else Movil()

        notificacion = (
            AlertaCritica(plataforma_obj)
            if tipo == "Crítica"
            else MensajeInformativo(plataforma_obj)
        )

        if st.button("Enviar"):
            st.success(notificacion.emitir(mensaje))

    # --- MEDIATOR ---
    elif opcion == "Mediator – Chat":
        st.header("Sala de Chat")

        if "sala" not in st.session_state:
            st.session_state.sala = SalaChat()

        nombre = st.text_input("Nombre", "Usuario_1")
        mensaje = st.text_area("Mensaje")

        if st.button("Enviar"):
            usuario = Usuario(nombre, st.session_state.sala)
            usuario.enviar(mensaje)

        st.subheader("Historial")
        for m in st.session_state.sala.historial:
            st.write(m)

    # --- DIAGRAMAS ---
    elif opcion == "Diagramas C4":
        mostrar_diagramas()
