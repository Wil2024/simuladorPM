iimport streamlit as st
import time

# --- Funciones de Simulación de IA ---
# Estas funciones simulan lo que haría un modelo de IA real.

def simular_analisis_riesgos(descripcion):
    """Simula la identificación de riesgos a partir de una descripción."""
    riesgos = {
        "riesgos_tecnicos": [
            "Integración fallida con sistemas heredados.",
            "Vulnerabilidades de seguridad no detectadas en la nueva plataforma.",
            "Rendimiento inferior al esperado bajo carga máxima."
        ],
        "riesgos_operacionales": [
            "Resistencia al cambio por parte de los usuarios finales.",
            "Capacitación insuficiente del personal.",
            "Retraso en la entrega de componentes por parte de proveedores clave."
        ],
        "riesgos_financieros": [
            "Sobrecostos debido a estimaciones de tiempo optimistas.",
            "Recorte de presupuesto a mitad del proyecto.",
            "Costos de licencia de software no contemplados."
        ]
    }
    # Lógica simple para personalizar la respuesta
    if "migración" in descripcion.lower():
        riesgos["riesgos_tecnicos"].append("Pérdida o corrupción de datos durante el proceso de migración.")
    if "app móvil" in descripcion.lower():
        riesgos["riesgos_tecnicos"].append("Problemas de compatibilidad con diferentes versiones de iOS/Android.")
    if "marketing" in descripcion.lower():
        riesgos["riesgos_operacionales"].append("Bajo engagement o recepción negativa de la campaña.")

    return riesgos

def simular_generacion_wbs(descripcion):
    """Simula la creación de una WBS/EDT."""
    wbs = "### Estructura de Desglose del Trabajo (WBS/EDT)\n\n"
    wbs += "1.  **Gestión del Proyecto**\n"
    wbs += "    1.1. Planificación y Diseño\n"
    wbs += "    1.2. Seguimiento y Control\n"
    wbs += "    1.3. Gestión de Riesgos\n"
    wbs += "    1.4. Cierre del Proyecto\n"
    wbs += "2.  **Fase de Análisis y Diseño**\n"
    wbs += "    2.1. Levantamiento de Requisitos\n"
    wbs += "    2.2. Diseño de la Arquitectura\n"
    wbs += "    2.3. Diseño de UI/UX\n"
    # Lógica simple para personalizar la respuesta
    if "app móvil" in descripcion.lower():
        wbs += "3.  **Fase de Desarrollo (App Móvil)**\n"
        wbs += "    3.1. Desarrollo del Backend y APIs\n"
        wbs += "    3.2. Desarrollo del Frontend iOS\n"
        wbs += "    3.3. Desarrollo del Frontend Android\n"
        wbs += "4.  **Fase de Pruebas y QA**\n"
        wbs += "    4.1. Pruebas Unitarias\n"
        wbs += "    4.2. Pruebas de Integración\n"
        wbs += "    4.3. Pruebas de Aceptación de Usuario (UAT)\n"
    elif "migración" in descripcion.lower():
        wbs += "3.  **Fase de Ejecución (Migración)**\n"
        wbs += "    3.1. Preparación del Entorno de Destino\n"
        wbs += "    3.2. Desarrollo de Scripts de Migración\n"
        wbs += "    3.3. Ejecución de Migración en Entorno de Pruebas\n"
        wbs += "    3.4. Ejecución de Migración en Producción\n"
        wbs += "4.  **Fase de Verificación Post-Migración**\n"
        wbs += "    4.1. Validación de Integridad de Datos\n"
        wbs += "    4.2. Pruebas de Rendimiento del Nuevo Sistema\n"
    else:
        wbs += "3.  **Fase de Ejecución/Implementación**\n"
        wbs += "4.  **Fase de Pruebas y Despliegue**\n"

    wbs += "5.  **Fase de Despliegue y Puesta en Marcha**\n"
    wbs += "    5.1. Capacitación a Usuarios\n"
    wbs += "    5.2. Puesta en Producción (Go-Live)\n"
    return wbs

def simular_asistente_comunicacion(descripcion, estado, audiencia):
    """Simula la redacción de un email de estado."""
    
    proyecto_nombre = "el proyecto"
    if "app móvil" in descripcion.lower():
        proyecto_nombre = "el proyecto de la App Móvil"
    elif "migración" in descripcion.lower():
        proyecto_nombre = "el proyecto de Migración de Datos"

    if estado == "A tiempo ✅":
        linea_estado = f"Me complace informar que {proyecto_nombre} avanza según lo planificado y estamos cumpliendo con los hitos clave."
        proximos_pasos = "Nuestros próximos pasos se centran en finalizar la fase actual y preparar el terreno para la siguiente etapa, tal como se definió en el cronograma."
    elif estado == "Con ligero retraso ⚠️":
        linea_estado = f"Quería ofrecer una actualización transparente sobre {proyecto_nombre}. Hemos encontrado algunos desafíos técnicos menores que han causado un ligero retraso en una de las tareas secundarias."
        proximos_pasos = "El equipo ya ha implementado un plan de mitigación y esperamos recuperar el tiempo perdido en los próximos días. El impacto en la fecha final del proyecto es nulo en este momento."
    else: # Con riesgo 🚨
        linea_estado = f"El motivo de esta comunicación es informar de manera proactiva sobre un riesgo identificado en {proyecto_nombre} que requiere nuestra atención."
        proximos_pasos = "Hemos detectado un posible bloqueo con un proveedor externo. Estamos trabajando en una solución y explorando alternativas. Sugiero una breve reunión para discutir el plan de contingencia."

    email = f"""
    **Asunto:** Actualización de Estado - {proyecto_nombre.title()}

    **Estimado/a {audiencia},**

    Espero que te encuentres muy bien.

    {linea_estado}

    **Logros Recientes:**
    - [Completar con el logro principal de la semana]
    - [Completar con un logro secundario]

    **Próximos Pasos:**
    {proximos_pasos}

    Agradezco de antemano tu continuo apoyo. No dudes en contactarme si tienes alguna consulta.

    Saludos cordiales,

    **[Tu Nombre]**
    Project Manager
    """
    return email


# --- Interfaz de Streamlit ---

st.set_page_config(page_title="Asistente IA para PMs", layout="wide")

# Título y Sidebar
st.title("🤖 Asistente de IA para Project Managers")
st.markdown("_Un simulador para demostrar cómo la IA potencia la gestión de proyectos._")

st.sidebar.header("Configuración del Proyecto")
descripcion_proyecto = st.sidebar.text_area(
    "Describe tu proyecto aquí:",
    "Lanzamiento de una nueva app móvil para e-commerce en iOS y Android, con integración a nuestro sistema de inventario actual. El objetivo es aumentar las ventas en un 15% en 6 meses.",
    height=150
)

herramienta_seleccionada = st.sidebar.selectbox(
    "Selecciona la herramienta de IA que quieres usar:",
    ["Análisis Predictivo de Riesgos", "Generador de WBS/EDT", "Asistente de Comunicaciones"]
)


# --- Lógica de la Interfaz Principal ---

if herramienta_seleccionada == "Análisis Predictivo de Riesgos":
    st.header("🔍 Análisis Predictivo de Riesgos")
    st.markdown("La IA analiza la descripción de tu proyecto para identificar posibles riesgos en diferentes categorías, permitiéndote ser más proactivo.")
    
    if st.button("Analizar Riesgos Ahora"):
        with st.spinner('La IA está analizando miles de proyectos pasados para encontrar patrones...'):
            time.sleep(2) # Simula el procesamiento
            riesgos = simular_analisis_riesgos(descripcion_proyecto)
        
        st.subheader("Resultados del Análisis:")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.warning("**Riesgos Técnicos**")
            for r in riesgos["riesgos_tecnicos"]:
                st.markdown(f"- {r}")
        with col2:
            st.warning("**Riesgos Operacionales**")
            for r in riesgos["riesgos_operacionales"]:
                st.markdown(f"- {r}")
        with col3:
            st.warning("**Riesgos Financieros**")
            for r in riesgos["riesgos_financieros"]:
                st.markdown(f"- {r}")

elif herramienta_seleccionada == "Generador de WBS/EDT":
    st.header("🏗️ Generador de WBS/EDT (Estructura de Desglose del Trabajo)")
    st.markdown("Ahorra horas de planificación. La IA crea una estructura WBS/EDT inicial basada en proyectos similares, que luego puedes refinar.")

    if st.button("Generar WBS/EDT"):
        with st.spinner('La IA está estructurando las fases y entregables del proyecto...'):
            time.sleep(2)
            wbs = simular_generacion_wbs(descripcion_proyecto)

        st.subheader("Propuesta de WBS/EDT:")
        st.markdown(wbs)


elif herramienta_seleccionada == "Asistente de Comunicaciones":
    st.header("✉️ Asistente de Comunicaciones para Stakeholders")
    st.markdown("La IA te ayuda a redactar comunicaciones claras, profesionales y con el tono adecuado, liberándote tiempo para la gestión estratégica.")

    st.subheader("Configura tu comunicación:")
    col1, col2 = st.columns(2)
    with col1:
        estado_actual = st.selectbox(
            "¿Cuál es el estado del proyecto?",
            ["A tiempo ✅", "Con ligero retraso ⚠️", "Con riesgo 🚨"]
        )
    with col2:
        audiencia = st.selectbox(
            "¿A quién va dirigido?",
            ["Comité Directivo", "Equipo Técnico", "Cliente Principal"]
        )
        
    if st.button("Redactar Borrador del Email"):
        with st.spinner('La IA está adaptando el tono y el mensaje...'):
            time.sleep(2)
            email = simular_asistente_comunicacion(descripcion_proyecto, estado_actual, audiencia)

        st.subheader("Borrador Sugerido por la IA:")
        st.markdown(email, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: grey;">
        <p>© 2025 | Creado por Wilton Torvisco</p>
    </div>
    """,
    unsafe_allow_html=True
)
