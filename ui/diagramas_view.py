import streamlit as st

def mostrar_diagramas():
    st.header("Entidad relación – UML")
    st.info(
        "A continuación se presentan los diagramas UML de clases"
        " que describen la estrucutra del sistema."
    )

    tab1, tab2, tab3 = st.tabs(
        ["Builder", "Bridge", "Mediator"]
    )

    with tab1:
        st.subheader("UML Builder")
        st.image(
            "diagrams/Uml-BuilderAutomovil.png",
            caption="Diagrama UML Builder",
            use_container_width=True
        )
        st.write(
            "Descripción de los diagramas"
            " continuacion de la descripción del diagrama."
        )

    with tab2:
        st.subheader("UML Bridge")
        st.image(
            "diagrams/UML-BridgeNotificaciones.png",
            caption="Diagrama UML Bridge",
            use_container_width=True
        )
        st.write(
            "Descripción del diagrama"
            " continuacion de la descripción del diagrama."
        )

    with tab3:
        st.subheader("UML Mediator")
        st.image(
            "diagrams/UML-MediatorSalaChat.png",
            caption="Diagrama UML Mediator",
            use_container_width=True
        )
        st.write(
            "Descripción del diagrama"
            " continuacion de la descripción del diagrama."
        )
