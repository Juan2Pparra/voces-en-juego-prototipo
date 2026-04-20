"""
ui/components.py
Componentes de interfaz para Voces en Juego.
"""

from html import escape
from textwrap import dedent

import streamlit as st
from core.codesign import EMOCION_EMOJI


def _html(s: str) -> str:
    return dedent(s).strip()


# ─────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────

def _chips(items: list, clase: str = "") -> str:
    if not items:
        return ""
    inner = "".join(
        f'<span class="chip {clase}">{escape(str(item))}</span>'
        for item in items
        if str(item).strip()
    )
    if not inner:
        return ""
    return f'<div class="chip-row">{inner}</div>'


def _obs_class(texto: str) -> str:
    t = str(texto).strip()
    if t.startswith("✅"):
        return "obs-ok"
    if t.startswith("⚠️"):
        return "obs-warn"
    if t.startswith("❌"):
        return "obs-err"
    return "obs-info"


def _card_header(icon: str, icon_color: str, title: str,
                 subtitle: str = "", badge: str = "") -> str:
    badge_html = (
        f'<span class="card-badge">{escape(str(badge))}</span>'
        if badge else ""
    )
    subtitle_html = (
        f'<div class="card-subtitle">{escape(str(subtitle))}</div>'
        if subtitle else ""
    )
    return _html(f"""
    <div class="card-header">
        <div class="card-icon {icon_color}">{icon}</div>
        <div>
            <div class="card-title">{escape(str(title))}</div>
            {subtitle_html}
        </div>
        {badge_html}
    </div>
    """)


def _card(title_html: str, body_html: str = "") -> str:
    return _html(f"""
    <div class="vej-card">
        {title_html}
        {body_html}
    </div>
    """)


# ─────────────────────────────────────────────────────
# TOPBAR
# ─────────────────────────────────────────────────────

def render_topbar():
    st.markdown(_html("""
    <div class="vej-topbar">
        <div class="vej-logo">
            <div class="vej-logo-dot">🎮</div>
            <span class="vej-logo-name">Voces en <em>Juego</em></span>
        </div>
        <div class="vej-breadcrumb">
            <a href="#">Proyectos</a>
            <span>›</span>
            <span>Arquitectura narrativa</span>
            <span>›</span>
            <span>Prototipo v1</span>
        </div>
    </div>
    """), unsafe_allow_html=True)


# ─────────────────────────────────────────────────────
# ENCABEZADO DE PÁGINA
# ─────────────────────────────────────────────────────

def render_page_header():
    st.markdown(_html("""
    <h1 class="page-title">Prototipo de generación narrativa</h1>
    <p class="page-subtitle">
        Valida la arquitectura de codiseño mediado por IA a partir del repositorio
        de memoria histórica del conflicto armado colombiano.
    </p>
    """), unsafe_allow_html=True)


# ─────────────────────────────────────────────────────
# STEPPER
# ─────────────────────────────────────────────────────

STEPS = [
    ("1", "Entrada"),
    ("2", "Codiseño"),
    ("3", "Control ético"),
    ("4", "Generación"),
    ("5", "Validación"),
]


def render_stepper(active_until: int = 0):
    items = []
    for i, (num, label) in enumerate(STEPS, start=1):
        if i < active_until:
            cls, circle = "step-item done", "✓"
        elif i == active_until:
            cls, circle = "step-item active", num
        else:
            cls, circle = "step-item", num

        items.append(
            f'<div class="{cls}"><span class="step-num">{circle}</span>{escape(label)}</div>'
        )
        if i < len(STEPS):
            items.append('<span class="step-sep">›</span>')

    st.markdown(
        f'<div class="stepper">{"".join(items)}</div>',
        unsafe_allow_html=True,
    )


# ─────────────────────────────────────────────────────
# PANEL DE ENTRADA
# ─────────────────────────────────────────────────────

def render_input_panel(historia_sel: dict):
    ep = historia_sel.get("emocion_principal") or {}
    es = historia_sel.get("emocion_secundaria") or {}

    emo1 = ep.get("emocion", "")
    emo2 = es.get("emocion", "")
    pct1 = round(ep.get("puntaje", 0) * 100)
    pct2 = round(es.get("puntaje", 0) * 100)

    titulo = historia_sel.get("titulo") or "N/A"
    ubicacion = historia_sel.get("ubicacion") or "No especificada"
    rol = (historia_sel.get("autor") or {}).get("rol") or "N/A"
    temas = historia_sel.get("temas") or []
    actores = historia_sel.get("actores") or []
    palabras = historia_sel.get("palabras_clave") or []
    frags = historia_sel.get("fragmentos") or []
    resumen = historia_sel.get("resumen") or ""

    emociones_items = []
    if emo1:
        emociones_items.append(f"{EMOCION_EMOJI.get(emo1, '●')} {emo1} · {pct1}%")
    if emo2:
        emociones_items.append(f"{EMOCION_EMOJI.get(emo2, '●')} {emo2} · {pct2}%")
    emo_chips = _chips(emociones_items, "emotion")

    row_temas = (
        f'<div class="meta-row"><span class="meta-label">Temas</span>{_chips(temas, "theme")}</div>'
        if temas else ""
    )
    row_actores = (
        f'<div class="meta-row"><span class="meta-label">Actores</span>{_chips(actores, "actor")}</div>'
        if actores else ""
    )
    row_palabras = (
        f'<div class="meta-row"><span class="meta-label">Palabras clave</span>{_chips(palabras, "keyword")}</div>'
        if palabras else ""
    )

    header = _card_header(
        "📂", "blue", "Entrada del sistema",
        "Repositorio narrativo · JSON", "Módulo 1.1–1.2"
    )

    body = _html(f"""
    <div class="meta-row">
        <span class="meta-label">Título</span>
        <span class="meta-value" style="font-weight:600;">{escape(str(titulo))}</span>
    </div>
    <div class="meta-row">
        <span class="meta-label">Ubicación</span>
        <span class="meta-value">{escape(str(ubicacion))}</span>
    </div>
    <div class="meta-row">
        <span class="meta-label">Autor / Rol</span>
        <span class="meta-value">{escape(str(rol))}</span>
    </div>
    <div class="meta-row">
        <span class="meta-label">Emociones detectadas</span>
        {emo_chips}
    </div>
    {row_temas}
    {row_actores}
    {row_palabras}
    """)

    st.markdown(_card(header, body), unsafe_allow_html=True)

    if frags:
        st.markdown(_html(f"""
        <div class="quote-block">
            <p class="quote-text">{escape(str(frags[0]))}</p>
        </div>
        """), unsafe_allow_html=True)

    if resumen:
        with st.expander("Ver resumen completo del relato"):
            st.markdown(
                f'<p style="font-size:0.88rem;color:#374151;line-height:1.7;margin:0;">{escape(str(resumen))}</p>',
                unsafe_allow_html=True,
            )


# ─────────────────────────────────────────────────────
# MÓDULO 1.3 – BLUEPRINT
# ─────────────────────────────────────────────────────

def render_blueprint(blueprint: dict):
    emo = blueprint.get("emocion_principal", "")
    emoji = EMOCION_EMOJI.get(emo, "●")

    header = _card_header(
        "🔀", "purple", "Módulo 1.3 — Codiseño indirecto",
        "Blueprint narrativo generado a partir del repositorio"
    )

    body = _html(f"""
    <div class="bp-grid">
        <div class="bp-cell">
            <div class="bp-cell-label">Tipo de escena</div>
            <div class="bp-cell-value">{escape(str(blueprint.get("tipo_escena", "")))}</div>
        </div>
        <div class="bp-cell">
            <div class="bp-cell-label">Tono narrativo</div>
            <div class="bp-cell-value">{escape(str(blueprint.get("tono", "")))}</div>
        </div>
        <div class="bp-cell highlight">
            <div class="bp-cell-label">Emoción base</div>
            <div class="bp-cell-value">{emoji} {escape(str(emo))}</div>
        </div>
    </div>
    <div class="objective-pill">
        <span class="objective-icon">🎯</span>
        <div>
            <div class="objective-label">Objetivo narrativo</div>
            <div class="objective-text">{escape(str(blueprint.get("objetivo_narrativo", "")))}</div>
        </div>
    </div>
    """)

    st.markdown(_card(header, body), unsafe_allow_html=True)


# ─────────────────────────────────────────────────────
# MÓDULO 1.4 – CONTROL ÉTICO
# ─────────────────────────────────────────────────────

def render_ethics(control: dict):
    header = _card_header(
        "🛡️", "green",
        "Módulo 1.4 — Control ético y Prompt Engineering",
        "Reglas de operación y prompt estructurado para el modelo"
    )

    st.markdown(_card(header), unsafe_allow_html=True)

    with st.expander("Ver las 7 reglas éticas aplicadas"):
        rules_html = "".join(
            f'<div class="rule-item"><span class="rule-check">✓</span><span>{escape(str(r))}</span></div>'
            for r in control.get("reglas_eticas", [])
        )
        st.markdown(rules_html, unsafe_allow_html=True)

    with st.expander("Ver prompt construido para el modelo de lenguaje"):
        prompt_safe = escape(str(control.get("prompt_construido", "")))
        st.markdown(
            f'<pre class="prompt-box">{prompt_safe}</pre>',
            unsafe_allow_html=True,
        )


# ─────────────────────────────────────────────────────
# MÓDULO 1.5 – GENERACIÓN NARRATIVA
# ─────────────────────────────────────────────────────

def render_generation(generado: dict):
    modo = generado.get("modo", "api")
    badge = "Generación local" if modo == "local" else ""
    badge_style = (
        'style="background:#fff7ed;border-color:#fde68a;color:#92400e;"'
        if modo == "local" else ""
    )
    badge_html = (
        f'<span class="card-badge" {badge_style}>{escape(str(badge))}</span>'
        if badge else ""
    )

    st.markdown(_html(f"""
    <div class="vej-card">
        <div class="card-header">
            <div class="card-icon blue">🤖</div>
            <div>
                <div class="card-title">Módulo 1.5 — Generación narrativa</div>
                <div class="card-subtitle">Escena · Diálogo NPC · Decisiones del jugador</div>
            </div>
            {badge_html}
        </div>
    </div>
    """), unsafe_allow_html=True)

    tab_escena, tab_dialogo, tab_decisiones = st.tabs(
        ["🏞️ Escena", "💬 Diálogo NPC", "🎯 Decisiones"]
    )

    with tab_escena:
        st.markdown(
            f'<div class="scene-box">{escape(str(generado.get("escena", "")))}</div>',
            unsafe_allow_html=True,
        )

    with tab_dialogo:
        dialogo = escape(str(generado.get("dialogo_npc", ""))).replace("\n", "<br>")
        st.markdown(
            f'<div class="npc-box">{dialogo}</div>',
            unsafe_allow_html=True,
        )

    with tab_decisiones:
        for linea in str(generado.get("decisiones", "")).splitlines():
            linea = linea.strip()
            if not linea:
                continue
            letra = linea[0] if linea[0] in "ABC" else "·"
            texto = linea[2:].strip() if len(linea) > 2 else linea
            st.markdown(_html(f"""
            <div class="decision-item">
                <span class="decision-letter">{escape(letra)}</span>
                <span class="decision-text">{escape(texto)}</span>
            </div>
            """), unsafe_allow_html=True)


# ─────────────────────────────────────────────────────
# MÓDULO 1.6 – VALIDACIÓN
# ─────────────────────────────────────────────────────

def render_validation(validacion: dict):
    color_map = {
        "green": ("#16a34a", "#22c55e"),
        "orange": ("#d97706", "#f59e0b"),
        "red": ("#dc2626", "#ef4444"),
    }
    text_color, bar_color = color_map.get(
        validacion.get("color"), ("#374151", "#9ca3af")
    )
    pct = validacion.get("puntuacion", 0)

    header = _card_header(
        "✅", "green",
        "Módulo 1.6 — Validación ética y narrativa",
        "Coherencia temática · Fidelidad contextual · Respeto ético"
    )

    st.markdown(_card(header), unsafe_allow_html=True)

    v1, v2 = st.columns([1, 2], gap="medium")

    with v1:
        estado_cls = escape(str(validacion.get("color", "green")))
        estado_txt = escape(str(validacion.get("estado", "")))
        st.markdown(_html(f"""
        <div class="score-card">
            <span class="score-value" style="color:{text_color};">{pct}</span>
            <span class="score-label">puntos / 100</span>
            <span class="score-estado {estado_cls}">{estado_txt}</span>
            <div class="score-bar-bg">
                <div class="score-bar-fill"
                     style="width:{pct}%;background:{bar_color};"></div>
            </div>
        </div>
        """), unsafe_allow_html=True)

    with v2:
        all_items = (
            [(o, _obs_class(o)) for o in validacion.get("observaciones", [])] +
            [(a, "obs-warn") for a in validacion.get("alertas", [])]
        )
        obs_html = "".join(
            f'<div class="obs-row {cls}">{escape(str(txt))}</div>'
            for txt, cls in all_items
        )
        st.markdown(obs_html, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────
# ESTADO INICIAL
# ─────────────────────────────────────────────────────

def render_idle_state():
    st.info(
        "Selecciona un relato del repositorio y presiona **Ejecutar pipeline** "
        "para ver la arquitectura en acción."
    )

    modules = [
        (
            "🔀", "blue", "Módulo 1.3 — Codiseño",
            "Convierte atributos del JSON (emoción, temas, actores) en un blueprint narrativo estructurado."
        ),
        (
            "🛡️", "green", "Módulo 1.4 — Control ético",
            "Define las 7 reglas éticas y construye el prompt final para el modelo de lenguaje."
        ),
        (
            "🤖", "purple", "Módulo 1.5 — Generación",
            "Produce escena, diálogo de NPC y 3 opciones de decisión a partir del prompt ético."
        ),
        (
            "✅", "amber", "Módulo 1.6 — Validación",
            "Evalúa coherencia, fidelidad contextual y respeto ético. Genera puntuación 0–100."
        ),
    ]

    items_html = "".join(
        _html(f"""
        <div class="module-preview">
            <div class="module-preview-icon card-icon {color}">{icon}</div>
            <div>
                <div class="module-preview-title">{escape(title)}</div>
                <div class="module-preview-desc">{escape(desc)}</div>
            </div>
        </div>
        """)
        for icon, color, title, desc in modules
    )

    st.markdown(
        f'<div class="modules-grid">{items_html}</div>',
        unsafe_allow_html=True,
    )