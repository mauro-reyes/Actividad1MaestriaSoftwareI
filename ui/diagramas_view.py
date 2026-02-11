import streamlit as st

def mostrar_diagramas():
    st.header("Arquitectura del Sistema – Modelo C4")
    st.info(
        "A continuación se presentan los diagramas C4 que describen la arquitectura "
        "del sistema desde el contexto hasta el nivel de componentes."
    )

    tab1, tab2, tab3 = st.tabs(
        ["Contexto", "Contenedores", "Componentes"]
    )

    with tab1:
        st.subheader("C4 – Nivel Contexto")
        st.image(
            "diagrams/c4_contexto.png",
            caption="Diagrama C4 – Nivel Contexto",
            use_container_width=True
        )
        st.write(
            "Describe la interacción entre el usuario y el sistema de demostración "
            "de patrones de diseño."
        )

    with tab2:
        st.subheader("C4 – Nivel Contenedores")
        st.image(
            "diagrams/c4_contenedores.png",
            caption="Diagrama C4 – Nivel Contenedores",
            use_container_width=True
        )
        st.write(
            "Muestra la separación entre la interfaz Streamlit y los módulos "
            "correspondientes a cada patrón de diseño."
        )

    with tab3:
        st.subheader("C4 – Nivel Componentes")
        st.image(
            "diagrams/c4_componentes.png",
            caption="Diagrama C4 – Nivel Componentes",
            use_container_width=True
        )
        st.write(
            "Detalla los componentes internos de los patrones Builder, Bridge y Mediator."
        )
