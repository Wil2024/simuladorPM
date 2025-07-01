import streamlit as st
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
s**")
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