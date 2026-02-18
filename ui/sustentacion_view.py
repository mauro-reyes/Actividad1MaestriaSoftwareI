import streamlit as st

def mostrar_sustentacion():
    st.header("Sustentación de Patrones de Diseño")
    st.info("A continuación se presenta la justificación de la selección de cada patrón para los ejercicios planteados.")

    tab1, tab2, tab3 = st.tabs(["Ejercicio 1 (Builder)", "Ejercicio 2 (Bridge)", "Ejercicio 3 (Mediator)"])

    with tab1:
        st.subheader("Ejercicio 1: Patrón Creacional - Builder")
        st.markdown("""
        **1. Identificación de la Categoría**
     
        Estamos ante un problema de Patrón Creacional, Porque el problema principal no es cómo estructurar clases (Estructural) ni cómo se comunican entre sí (Comportamiento), sino cómo crear un objeto complejo de manera flexible y limpia. El problema lo encontramos en el mecanismo de inicialización del objeto Automóvil.

        **2. Selección del Patrón**
       
        
        * El patrón que se adecúa perfectamente a esta solución es el Builder (Constructor), porque la descripción del ejercicio menciona el problema del "constructor telescópico" (muchos parámetros opcionales), y específicamente utilizamos el patron Builder para evitar un 'constructor telescópico. 
        
        * El patrón Builder sugiere sacar el código de construcción del objeto de su propia clase y colocarlo dentro de objetos independientes llamados constructores (builders), nos permite construir objetos complejos paso a paso, lo importante aquí es que no necesitamos invocar todos los pasos, podemos llamar solo a aquellos necesarios para producir una configuración particular del objeto como por ejemplo un carro con GPS pero sin techo solar.
        
        
        **3. Cumplimiento de Requisitos**
        a.  **Legibilidad y Claridad**: En lugar de llamar a new Auto(V8, Rojo, null, null, true, ...), utilizamos métodos legibles, ya no hace falta agregar muchos parámetros innecesarios dentro de los constructores.
        b.  **Flexibilidad (Configuraciones opcionales)**: El patrón permite construir el objeto paso a paso, Podemos aplazar la ejecución de ciertos pasos sin descomponer el producto final.
        c.  **Separación de construcción y representación**: El patrón aísla el código de construcción complejo de la lógica de negocio y del producto en sí.

        **4. ¿Por qué descartamos otros patrones?**
        *   *¿Por qué no Abstract Factory?* El Abstract Factory se especializa en crear familias de objetos relacionados (ej. Silla Victoriana + Sofá Victoriano), en este ejercicio el problema no es la compatibilidad entre familias de productos, sino la complejidad de configurar un solo objeto
        
        *   *¿Por qué no Factory Method?* Factory Method podria sernos útil, pero generalmente crea objetos en un solo paso. no soluciona el problema del "constructor telescópico" si el objeto requiere muchos parámetros de inicialización.
        """)

    with tab2:
        st.subheader("Ejercicio 2: Patrón Estructural - Bridge")
        st.markdown("""
        **1. Identificación de la Categoría**

        Estamos ante un problema de Patrón Estructural, porque el problema no es cómo se crean los objetos, sino cómo se engranan las clases para evitar una estructura poco flexible y muy grande, este ejercicio describe la necesidad de extender una clase en dos dimensiones independientes (Tipo de Notificación y Plataforma), lo cual es el caso de uso preciso para esta categoría.
        
        **2. Selección del Patrón**
       
        * El patrón que se adecúa perfectamente a esta solución es el de Bridge (Puente) ya que el patrón Bridge está diseñado específicamente para dividir una clase grande o un grupo de clases estrechamente relacionadas en dos jerarquías separadas (abstracción e implementación) que pueden desarrollarse independientemente, esto ataca directamente al problema de "explosión combinatoria" de subclases.

        * El patrón sugiere pasar de la herencia a la composición, en lugar de tener una superclase Notificación que intenta manejar todas las variaciones, extraemos una de las dimensiones (la Plataforma) a una jerarquía de clases separada. La clase Notificación (Abstracción) contendrá un campo de referencia a un objeto Plataforma (Implementación), la notificación delega el trabajo real de "enviar/mostrar" al objeto de plataforma vinculado.

        **3. Cumplimiento de Requisitos**
        1.  **Separación de responsabilidades**: Dividimos la lógica de la notificación (Abstracción) de la lógica de la plataforma (Implementación), podemos cambiar la interfaz gráfica o la lógica de negocio sin tocar el código de la API de la plataforma.
        2.  **Reducción de clases**: Evitamos la multiplicacion de clases, si por ejemplo tenemos 4 tipos de notificaciones y 3 plataformas:
            *   Sin Bridge: 4 tipos x 3 plataformas = 12 subclases.
            *   Con Bridge: 4 + 3 = 7 clases. Añadir una plataforma suma 1 clase, no 4.
        3.  **Flexibilidad en tiempo de ejecución**: Podemos cambiar la plataforma dinámicamente si es necesario, por ejemplo, cambiar de Modo Escritorio a Modo Móvil en caliente simplemente asignando un nuevo objeto al campo de referencia.

        **4. ¿Por qué descartamos otros patrones?**
        *   *¿Por qué no Adapter?* El Adapter se usa para hacer que clases incompatibles trabajen juntas, normalmente con código existente (legacy). El Bridge se diseña por anticipado para evitar que la arquitectura se vuelva rígida.

        *   *¿Por qué no Decorator?* El Decorator añade responsabilidades al objeto, pero mantiene la misma interfaz y no suele separar la abstracción de la implementación en dos jerarquías distintas para desarrollarlas por separado.
        """)

    with tab3:
        st.subheader("Ejercicio 3: Patrón de Comportamiento - Mediator")
        st.markdown("""
        **1. Identificación de la Categoría**
       
       Estamos ante un problema de Patrón de Comportamiento, porque el desafío no es cómo se crean los usuarios ni cómo se estructura la clase Usuario en si, sino cómo se comunican y asignan responsabilidades entre ellos, el problema es el flujo de mensajes y la gestión de las interacciones.

        **2. Selección del Patrón**
        
        * El patrón que se adecúa perfectamente a esta solución es el Mediator (Mediador, porque el ejercicio describe literalmente el propósito de este patrón, que es reducir las dependencias caóticas entre objetos y restringir las comunicaciones directas, forzándolos a colaborar únicamente a través de un objeto mediador.
        
        * El patrón Mediator sugiere que no hagamos comunicación directa entre los componentes que queremos hacer independientes entre sí (en este caso, los Usuarios), en cambio, estos componentes colaboran indirectamente invocando a un objeto mediador especial que redirecciona las llamadas a los componentes adecuados, los componentes (Usuarios) dependen únicamente de la clase mediadora, en lugar de estar acoplados a decenas de clases.

        **3. Cumplimiento de Requisitos**
        1.  **Facilita el mantenimiento**: Al agregar un nuevo usuario, solo necesitmos registrarlo en la SalaDeChat (Mediador) no tenemos que ir usuario por usuario actualizando sus listas de contactos, los componentes no conocen otros componentes.
        2.  **Mejor organización (Lógica centralizada)**: Toda la lógica de quién recibe el mensaje o qué pasa si el usuario está silenciado vive en el Mediador, no regada en la clase Usuario.
        3.  **Reduce la complejidad**: Transformamos una relación de "muchos a muchos" (una red enmarañada) en una relación de "uno a muchos" (estrella), donde todos apuntan al centro, esto elimina las dependencias caóticas como se le dicen.

        **4. ¿Por qué descartamos otros patrones?**
        *   *¿Por qué no Observer?* El Observer se usa para que objetos se suscriban dinámicamente a cambios de estado de otro. Aunque un chat podría usar Observer (los usuarios "observan" la sala), el Observer no encapsula la lógica de interacción compleja.

        *   *¿Por qué no Chain of Responsibility?* Este patrón pasa una solicitud secuencialmente por una cadena hasta que alguien la procesa. En un chat, cuando envías un mensaje, no queremos que pase de usuario en usuario hasta que alguien lo lea, queremos que el mediador lo distribuya a los destinatarios correctos inmediatamente.
        """)
