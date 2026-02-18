# Actividad 1 - Patrones de Diseño de Software

Este repositorio contiene la solución para la **Actividad 1: Patrones de Diseño** de la Maestría en Arquitectura de Software. El proyecto implementa y demuestra tres patrones de diseño fundamentales utilizando Python y una interfaz interactiva desarrollada en Streamlit.

## Integrantes del Grupo
*   **Abdul Mauricio Reyes**
*   **Wilmer Ricardo Castro Delgadillo**
*   **Luis Felipe Mora Lobo**
*   **Manuel Alejandro Ovalle**

## Descripción del Proyecto

El objetivo de esta actividad es identificar, seleccionar, diseñar e implementar soluciones para tres ejercicios prácticos, aplicando patrones de diseño. La aplicación incluye:

1.  **Patrón Creacional (Builder)**: Implementación de un configurador de automóviles paso a paso, abordando el problema del "constructor telescópico".
2.  **Patrón Estructural (Bridge)**: Sistema de notificaciones que desacopla la abstracción (tipo de mensaje) de la implementación (plataforma de envío), evitando la explosión de subclases.
3.  **Patrón de Comportamiento (Mediator)**: Sala de chat centralizada que gestiona la comunicación entre usuarios, reduciendo el acoplamiento directo entre ellos.
4.  **Diagramas de Clases (UML)**: Visualización de la estructura de las soluciones.
5.  **Sustentación**: Justificación detallada de la selección de cada patrón.

## Tecnologías Utilizadas

*   **Lenguaje**: Python 3.10+
*   **Framework Web**: Streamlit

## Guía de Instalación y Ejecución

Siga estos pasos para descargar y ejecutar la aplicación en su entorno local:

### 1. Clonar el Repositorio (u obtener el código)

Se tiene acceso al repositorio git:
```bash
git clone https://github.com/mauro-reyes/Actividad1MaestriaSoftwareI.git
cd Actividad1MaestriaSoftwareI
```
Si tiene el código comprimido (`.zip`), descomprímalo y navegue a la carpeta raíz del proyecto en tu terminal.

### 2. Crear un Entorno Virtual (Recomendado)

Es buena práctica aislar las dependencias del proyecto.

**En macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**En Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Instalar Dependencias

Asegúrese de que `pip` esté actualizado e instala los requerimientos:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```
*Si no tienes el archivo `requirements.txt`, puedes instalar manualmente:*
```bash
pip install streamlit pypdf
```

### 4. Ejecutar la Aplicación

Despliegue el servidor de Streamlit con el siguiente comando:

```bash
python3 -m streamlit run main.py
```

### 5. Acceder a la Aplicación

Una vez ejecutado el comando, Streamlit abrirá automáticamente la aplicación en su navegador por defecto. Si no lo hace, accede manualmente a la URL que se muestra en la terminal, usualmente:

*   **Local URL**: http://localhost:8501
