"""
app.py — Voces en Juego · Prototipo de arquitectura narrativa
Flujo: Repositorio → 1.3 Codiseño → 1.4 Control ético → 1.5 Generación → 1.6 Validación
"""

import streamlit as st

# ── Configuración de página (debe ir PRIMERO) ──────────────────
st.set_page_config(
    page_title="Voces en Juego – Prototipo",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Módulos del núcleo ─────────────────────────────────────────
from core.loader     import cargar_historias, cargar_textos, cargar_fuentes
from core.codesign   import modulo_1_3_codiseno
from core.ethics     import modulo_1_4_control_etico
from core.generation import modulo_1_5_generacion
from core.validation import modulo_1_6_validacion
from core.exporter   import exportar_resultado

# ── Módulos de UI ──────────────────────────────────────────────
from ui.styles     import load_styles
from ui.components import (
    render_topbar,
    render_page_header,
    render_stepper,
    render_input_panel,
    render_blueprint,
    render_ethics,
    render_generation,
    render_validation,
    render_idle_state,
)

# ══════════════════════════════════════════════════════════════
# ESTILOS
# ══════════════════════════════════════════════════════════════
load_styles()

# ══════════════════════════════════════════════════════════════
# TOPBAR + ENCABEZADO
# ══════════════════════════════════════════════════════════════
render_topbar()
render_page_header()

# ══════════════════════════════════════════════════════════════
# CARGA DE DATOS
# ══════════════════════════════════════════════════════════════
historias = cargar_historias()
_ = cargar_textos()
_ = cargar_fuentes()

titulos = {h["titulo"]: h for h in historias}

# ══════════════════════════════════════════════════════════════
# SELECTOR DE HISTORIA
# ══════════════════════════════════════════════════════════════
titulo_sel = st.selectbox(
    "Seleccionar historia del repositorio narrativo",
    list(titulos.keys()),
    index=0,
)
historia_sel = titulos[titulo_sel]

st.markdown("<br>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# LAYOUT PRINCIPAL: entrada (izq) + pipeline (der)
# ══════════════════════════════════════════════════════════════
col_entrada, col_pipeline = st.columns([1, 2], gap="large")

with col_entrada:
    render_input_panel(historia_sel)

with col_pipeline:

    # ── Botón de ejecución ─────────────────────────────────────
    ejecutar = st.button("▶  Ejecutar pipeline completo", use_container_width=True)

    if ejecutar:

        # ──────────────────────────────────────────────────────
        # MÓDULO 1.3 – CODISEÑO
        # ──────────────────────────────────────────────────────
        render_stepper(active_until=2)
        blueprint = modulo_1_3_codiseno(historia_sel)
        render_blueprint(blueprint)

        # ──────────────────────────────────────────────────────
        # MÓDULO 1.4 – CONTROL ÉTICO
        # ──────────────────────────────────────────────────────
        render_stepper(active_until=3)
        control = modulo_1_4_control_etico(historia_sel, blueprint)
        render_ethics(control)

        # ──────────────────────────────────────────────────────
        # MÓDULO 1.5 – GENERACIÓN
        # ──────────────────────────────────────────────────────
        render_stepper(active_until=4)
        with st.spinner("Generando contenido narrativo…"):
            generado = modulo_1_5_generacion(
                control["prompt_construido"], historia_sel, blueprint
            )

        # Advertencia si hubo error de API y se usó fallback
        if generado.get("error_api"):
            st.warning(
                f"⚠️ La API no respondió ({generado['error_api'][:80]}…). "
                "Se usó el generador local como respaldo."
            )

        render_generation(generado)

        # ──────────────────────────────────────────────────────
        # MÓDULO 1.6 – VALIDACIÓN
        # ──────────────────────────────────────────────────────
        render_stepper(active_until=5)
        validacion = modulo_1_6_validacion(generado, blueprint, historia_sel)
        render_validation(validacion)

        # ──────────────────────────────────────────────────────
        # EXPORTAR
        # ──────────────────────────────────────────────────────
        st.markdown("<hr>", unsafe_allow_html=True)
        resultado_txt = exportar_resultado(
            historia_sel, blueprint, control, generado, validacion
        )
        st.download_button(
            label="↓  Exportar resultado como .txt",
            data=resultado_txt,
            file_name=f"vej_{titulo_sel[:28].replace(' ', '_')}.txt",
            mime="text/plain",
            use_container_width=True,
        )

        modo_label = "API Claude" if generado.get("modo") == "api" else "generador local"
        st.success(f"✓  Pipeline ejecutado correctamente · {modo_label}")

    else:
        # Estado inicial: stepper en paso 1 + resumen de módulos
        render_stepper(active_until=1)
        render_idle_state()