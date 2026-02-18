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
            "diagrams/Pattern Builder- Automovil.png",
            caption="Diagrama UML Builder",
            use_container_width=True
        )
        st.markdown(
            """
            ### Lectura del Diagrama
            Al observar el diagrama, vemos que la clase `AutomovilBuilderConcreto` hereda de la interfaz `AutomovilBuilder`. Esto significa que el concreto *es un* tipo de constructor que debe cumplir con el contrato definido. A su vez, notamos una línea punteada que va desde el Builder hacia `Automovil`, indicando que el objetivo final de este constructor es crear instancias de `Automovil`, el cual es nuestro producto complejo.

            ### Análisis Arquitectónico
            El patrón Builder nos permite separar la construcción de un objeto de su representación final, podemos observar cómo `Automovil` mantiene sus propiedades encapsuladas (privadas, marcadas con el guion `-`), y solo son accesibles mediante métodos controlados. Esto garantiza que nadie pueda alterar el estado del auto de forma indebida una vez construido.

            ### Cumplimiento de Principios SOLID
            *   **SRP (Principio de Responsabilidad Única)**: La clase `Automovil` es puramente un contenedor de datos, mientras que toda la lógica de "cómo se crea" reside exclusivamente en el Builder.
            *   **OCP (Principio Abierto/Cerrado)**: El diseño está listo para crecer. Podríamos agregar un nuevos constructores sin necesidad de modificar el código existente de la clase `Automovil`.
            """
        )

    with tab2:
        st.subheader("UML Bridge")
        st.image(
            "diagrams/Pattern Bridge - Notificaciones.png",
            caption="Diagrama UML Bridge",
            use_container_width=True
        )
        st.markdown(
            """
            ### Lectura del Diagrama
            En este diagrama se aprecia claramente la división estructural en dos grupos. Por un lado, tenemos la jerarquía de `Notificacion` (la Abstracción) y por el otro la de `Plataforma` (la Implementación). La línea con el rombo blanco nos dice que una Notificación *tiene* una Plataforma internamente, pero gracias a que `Plataforma` es una interfaz, no estamos atados a una implementación específica.

            ### Análisis Arquitectónico
            Este diseño es fundamental para mantener el sistema limpio. En lugar de crear una clase combinada para cada caso (como "AlertaWeb", "AlertaMovil", "MensajeWeb"...), separamos las responsabilidades. Esto permite que los tipos de notificación y las plataformas de envío evolucionen por separado sin afectarse mutuamente.

            ### Cumplimiento de Principios SOLID
            *   **DIP (Principio de Inversión de Dependencias)**: Es evidente en el constructor: la `Notificacion` no depende de `Web` o `Movil` concretamente, sino de la abstracción `Plataforma`. Esto hace al sistema extremadamente flexible.
            *   **OCP (Principio Abierto/Cerrado)**: Puedes agregar nuevas plataformas (como Slack o Email) creando nuevas subclases, y el sistema de notificaciones las aceptará sin cambiar una sola línea de código.
            """
        )

    with tab3:
        st.subheader("UML Mediator")
        st.image(
            "diagrams/Pattern Mediator - Sala Chat.png",
            caption="Diagrama UML Mediator",
            use_container_width=True
        )
        st.markdown(
            """
            ### Lectura del Diagrama
            El diagrama nos muestra a `SalaChat` como el centro neurálgico de la comunicación. Las flechas indican una relación: la Sala *conoce* (agrega) a múltiples objetos `Usuario`, y a su vez, cada `Usuario` tiene una referencia hacia la `Sala`. Es una relación bidireccional necesaria para que este patrón funcione.

            ### Análisis Arquitectónico
            El Mediador centraliza toda la lógica de comunicación. Los usuarios no necesitan conectarse entre ellos directamente; solo "hablan" con la sala. Esto transforma una potencial "red de araña" (todos contra todos) en una estructura de estrella, mucho más ordenada y fácil de mantener.

            ### Cumplimiento de Principios SOLID
            *   **SRP (Principio de Responsabilidad Única)**: Cada `Usuario` solamente se preocupa por su propio mensaje. Delega completamente la responsabilidad de "a quién se lo envío" o "quién más está en la sala" a la clase `SalaChat`.
            *   **Desacoplamiento**: Si en el futuro cambiamos cómo se distribuyen los mensajes, solo tocaremos la `SalaChat`, y los usuarios ni se enterarán.
            """
        )
