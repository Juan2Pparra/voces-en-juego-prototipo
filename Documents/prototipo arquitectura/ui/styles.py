import streamlit as st


def load_styles():
    st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">

<style>
/* ══════════════════════════════════════════════
   RESET Y BASE — fondo blanco, estilo SaaS limpio
   ══════════════════════════════════════════════ */
*, *::before, *::after { box-sizing: border-box; }

:root {
    --bg:         #f7f8fa;
    --surface:    #ffffff;
    --border:     #e8eaed;
    --border-md:  #d1d5db;
    --text-1:     #111827;
    --text-2:     #374151;
    --text-3:     #6b7280;
    --text-4:     #9ca3af;
    --accent:     #2563eb;
    --accent-bg:  #eff6ff;
    --accent-2:   #7c3aed;
    --accent-2bg: #f5f3ff;
    --success:    #16a34a;
    --success-bg: #f0fdf4;
    --warn:       #d97706;
    --warn-bg:    #fffbeb;
    --danger:     #dc2626;
    --danger-bg:  #fef2f2;
    --radius-sm:  6px;
    --radius:     10px;
    --radius-lg:  14px;
    --shadow-sm:  0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
    --shadow:     0 4px 12px rgba(0,0,0,0.07), 0 2px 4px rgba(0,0,0,0.04);
}

html, body,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > .main {
    background: var(--bg) !important;
    font-family: 'DM Sans', system-ui, sans-serif !important;
    color: var(--text-1) !important;
}

[data-testid="stHeader"] { background: transparent !important; }

.block-container {
    padding: 2rem 2.5rem 4rem !important;
    max-width: 1380px !important;
}

/* ══════════════════════════════════════════════
   SIDEBAR FALSA — BARRA SUPERIOR DE NAVEGACIÓN
   ══════════════════════════════════════════════ */
.vej-topbar {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0 0 1.6rem 0;
    border-bottom: 1px solid var(--border);
    margin-bottom: 1.8rem;
}

.vej-logo {
    display: flex;
    align-items: center;
    gap: 0.55rem;
    font-family: 'DM Serif Display', Georgia, serif;
    font-size: 1.25rem;
    color: var(--text-1);
    letter-spacing: -0.01em;
    text-decoration: none;
}

.vej-logo-dot {
    width: 28px;
    height: 28px;
    background: var(--accent);
    border-radius: 7px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.85rem;
    color: white;
    flex-shrink: 0;
}

.vej-logo-name { color: var(--text-1); }
.vej-logo-name em { color: var(--accent); font-style: normal; }

.vej-breadcrumb {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    font-size: 0.82rem;
    color: var(--text-4);
    margin-left: auto;
}

.vej-breadcrumb a { color: var(--accent); text-decoration: none; }
.vej-breadcrumb span { color: var(--text-4); }

/* ══════════════════════════════════════════════
   ENCABEZADO DE PÁGINA
   ══════════════════════════════════════════════ */
.page-title {
    font-family: 'DM Serif Display', Georgia, serif;
    font-size: 1.85rem;
    font-weight: 400;
    color: var(--text-1);
    letter-spacing: -0.02em;
    margin: 0 0 0.3rem 0;
    line-height: 1.15;
}

.page-subtitle {
    font-size: 0.9rem;
    color: var(--text-3);
    font-weight: 400;
    line-height: 1.55;
    margin: 0 0 1.8rem 0;
    max-width: 600px;
}

/* ══════════════════════════════════════════════
   BARRA DE FLUJO — STEPPER HORIZONTAL
   ══════════════════════════════════════════════ */
.stepper {
    display: flex;
    align-items: center;
    gap: 0;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 0.1rem;
    margin-bottom: 2rem;
    overflow: hidden;
    box-shadow: var(--shadow-sm);
}

.step-item {
    flex: 1;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.65rem 0.9rem;
    border-radius: var(--radius);
    font-size: 0.8rem;
    font-weight: 500;
    color: var(--text-4);
    transition: all 0.15s;
    white-space: nowrap;
}

.step-item.done {
    color: var(--text-2);
}

.step-item.active {
    background: var(--accent-bg);
    color: var(--accent);
    font-weight: 600;
}

.step-num {
    width: 22px;
    height: 22px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.7rem;
    font-weight: 700;
    background: var(--border);
    color: var(--text-3);
    flex-shrink: 0;
    transition: all 0.15s;
}

.step-item.done .step-num {
    background: var(--success-bg);
    color: var(--success);
}

.step-item.active .step-num {
    background: var(--accent);
    color: white;
}

.step-sep {
    color: var(--border-md);
    font-size: 0.75rem;
    padding: 0 0.1rem;
    flex-shrink: 0;
}

/* ══════════════════════════════════════════════
   TARJETAS / SECCIONES
   ══════════════════════════════════════════════ */
.vej-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 1.4rem;
    margin-bottom: 1rem;
    box-shadow: var(--shadow-sm);
}

.card-header {
    display: flex;
    align-items: center;
    gap: 0.65rem;
    padding-bottom: 1rem;
    margin-bottom: 1rem;
    border-bottom: 1px solid var(--border);
}

.card-icon {
    width: 32px;
    height: 32px;
    border-radius: var(--radius-sm);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.95rem;
    flex-shrink: 0;
}

.card-icon.blue  { background: var(--accent-bg); }
.card-icon.green { background: var(--success-bg); }
.card-icon.purple{ background: var(--accent-2bg); }
.card-icon.amber { background: var(--warn-bg); }

.card-title {
    font-size: 0.88rem;
    font-weight: 700;
    color: var(--text-1);
    line-height: 1.2;
}

.card-subtitle {
    font-size: 0.75rem;
    color: var(--text-3);
    margin-top: 0.1rem;
}

.card-badge {
    margin-left: auto;
    font-size: 0.7rem;
    font-weight: 600;
    padding: 0.2rem 0.6rem;
    border-radius: 999px;
    background: var(--accent-bg);
    color: var(--accent);
    border: 1px solid #bfdbfe;
    white-space: nowrap;
}

/* ══════════════════════════════════════════════
   FILAS DE METADATOS
   ══════════════════════════════════════════════ */
.meta-row {
    display: flex;
    flex-direction: column;
    gap: 0.12rem;
    padding: 0.6rem 0;
    border-bottom: 1px solid #f3f4f6;
}
.meta-row:last-child { border-bottom: none; }

.meta-label {
    font-size: 0.7rem;
    font-weight: 600;
    color: var(--text-4);
    text-transform: uppercase;
    letter-spacing: 0.06em;
}

.meta-value {
    font-size: 0.9rem;
    color: var(--text-1);
    font-weight: 400;
    line-height: 1.45;
}

/* ══════════════════════════════════════════════
   CHIPS / BADGES
   ══════════════════════════════════════════════ */
.chip-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem;
    padding-top: 0.2rem;
}

.chip {
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
    padding: 0.22rem 0.65rem;
    border-radius: 999px;
    font-size: 0.74rem;
    font-weight: 500;
    border: 1px solid var(--border);
    background: var(--bg);
    color: var(--text-2);
}

.chip.emotion { background: #ecfdf5; border-color: #a7f3d0; color: #065f46; }
.chip.theme   { background: var(--accent-2bg); border-color: #ddd6fe; color: var(--accent-2); }
.chip.actor   { background: var(--accent-bg); border-color: #bfdbfe; color: #1e40af; }
.chip.keyword { background: #fff7ed; border-color: #fed7aa; color: #92400e; }

/* ══════════════════════════════════════════════
   CITA / FRAGMENTO TESTIMONIAL
   ══════════════════════════════════════════════ */
.quote-block {
    position: relative;
    background: #fafafa;
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent-2);
    border-radius: 0 var(--radius) var(--radius) 0;
    padding: 1rem 1rem 1rem 1.2rem;
    margin-top: 0.5rem;
}

.quote-block::before {
    content: '"';
    position: absolute;
    top: 0.2rem;
    left: 0.8rem;
    font-family: 'DM Serif Display', serif;
    font-size: 2.8rem;
    color: var(--accent-2);
    opacity: 0.18;
    line-height: 1;
    pointer-events: none;
}

.quote-text {
    font-size: 0.88rem;
    color: var(--text-2);
    font-style: italic;
    line-height: 1.7;
    margin: 0;
}

/* ══════════════════════════════════════════════
   BLUEPRINT GRID
   ══════════════════════════════════════════════ */
.bp-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.7rem;
    margin-bottom: 1rem;
}

.bp-cell {
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 0.85rem;
}

.bp-cell-label {
    font-size: 0.68rem;
    font-weight: 600;
    color: var(--text-4);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 0.35rem;
}

.bp-cell-value {
    font-size: 0.88rem;
    font-weight: 600;
    color: var(--text-1);
    line-height: 1.35;
}

.bp-cell.highlight {
    background: var(--accent-bg);
    border-color: #bfdbfe;
}

.bp-cell.highlight .bp-cell-value { color: var(--accent); }

/* ══════════════════════════════════════════════
   OBJETIVO NARRATIVO
   ══════════════════════════════════════════════ */
.objective-pill {
    display: flex;
    align-items: flex-start;
    gap: 0.65rem;
    background: var(--warn-bg);
    border: 1px solid #fde68a;
    border-radius: var(--radius);
    padding: 0.85rem 1rem;
}

.objective-icon {
    font-size: 1rem;
    flex-shrink: 0;
    margin-top: 0.05rem;
}

.objective-label {
    font-size: 0.68rem;
    font-weight: 700;
    color: var(--warn);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-bottom: 0.2rem;
}

.objective-text {
    font-size: 0.88rem;
    color: #78350f;
    line-height: 1.55;
}

/* ══════════════════════════════════════════════
   REGLAS ÉTICAS
   ══════════════════════════════════════════════ */
.rule-item {
    display: flex;
    align-items: flex-start;
    gap: 0.6rem;
    padding: 0.5rem 0;
    border-bottom: 1px solid #f9fafb;
    font-size: 0.85rem;
    color: var(--text-2);
    line-height: 1.5;
}

.rule-item:last-child { border-bottom: none; }

.rule-check {
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: var(--success-bg);
    border: 1px solid #bbf7d0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.6rem;
    color: var(--success);
    flex-shrink: 0;
    margin-top: 0.15rem;
}

/* ══════════════════════════════════════════════
   PROMPT BOX
   ══════════════════════════════════════════════ */
.prompt-box {
    background: #0f1117;
    color: #a3e635;
    border-radius: var(--radius);
    padding: 1rem 1.2rem;
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
    font-size: 0.78rem;
    line-height: 1.7;
    white-space: pre-wrap;
    word-break: break-word;
    overflow-x: auto;
    border: 1px solid #1e2535;
    max-height: 300px;
    overflow-y: auto;
}

/* ══════════════════════════════════════════════
   CONTENIDO GENERADO
   ══════════════════════════════════════════════ */
.scene-box {
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent);
    border-radius: 0 var(--radius) var(--radius) 0;
    padding: 1.1rem 1.2rem;
    font-size: 0.92rem;
    color: var(--text-2);
    line-height: 1.8;
}

.npc-box {
    background: #fffbeb;
    border: 1px solid #fde68a;
    border-left: 3px solid #f59e0b;
    border-radius: 0 var(--radius) var(--radius) 0;
    padding: 1.1rem 1.2rem;
    font-family: 'DM Serif Display', serif;
    font-style: italic;
    font-size: 1.05rem;
    color: #78350f;
    line-height: 1.75;
}

.decision-item {
    display: flex;
    align-items: flex-start;
    gap: 0.8rem;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 0.9rem 1rem;
    margin-bottom: 0.55rem;
    transition: border-color 0.15s, box-shadow 0.15s;
    cursor: default;
}

.decision-item:hover {
    border-color: var(--accent);
    box-shadow: 0 0 0 3px rgba(37,99,235,0.06);
}

.decision-letter {
    width: 28px;
    height: 28px;
    border-radius: var(--radius-sm);
    background: var(--accent-bg);
    border: 1px solid #bfdbfe;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.78rem;
    font-weight: 700;
    color: var(--accent);
    flex-shrink: 0;
}

.decision-text {
    font-size: 0.88rem;
    color: var(--text-2);
    line-height: 1.55;
    padding-top: 0.25rem;
}

/* ══════════════════════════════════════════════
   VALIDACIÓN
   ══════════════════════════════════════════════ */
.score-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 1.5rem 1rem;
    text-align: center;
    box-shadow: var(--shadow-sm);
}

.score-value {
    font-family: 'DM Serif Display', serif;
    font-size: 4rem;
    line-height: 1;
    display: block;
    margin-bottom: 0.3rem;
}

.score-label {
    font-size: 0.72rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-4);
    margin-bottom: 0.8rem;
    display: block;
}

.score-estado {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    font-size: 0.8rem;
    font-weight: 700;
    padding: 0.3rem 0.9rem;
    border-radius: 999px;
}

.score-estado.green  { background: var(--success-bg); color: var(--success); border: 1px solid #bbf7d0; }
.score-estado.orange { background: var(--warn-bg);    color: var(--warn);    border: 1px solid #fde68a; }
.score-estado.red    { background: var(--danger-bg);  color: var(--danger);  border: 1px solid #fecaca; }

.score-bar-bg {
    height: 5px;
    background: var(--border);
    border-radius: 3px;
    margin-top: 1.2rem;
    overflow: hidden;
}

.score-bar-fill {
    height: 100%;
    border-radius: 3px;
    transition: width 0.8s ease;
}

.obs-row {
    display: flex;
    align-items: flex-start;
    gap: 0.6rem;
    padding: 0.6rem 0.8rem;
    border-radius: var(--radius-sm);
    margin-bottom: 0.4rem;
    font-size: 0.85rem;
    color: var(--text-2);
    line-height: 1.5;
}

.obs-ok   { background: var(--success-bg); }
.obs-info { background: var(--bg); border: 1px solid var(--border); }
.obs-warn { background: var(--warn-bg); color: #78350f; }
.obs-err  { background: var(--danger-bg); color: #7f1d1d; }

/* ══════════════════════════════════════════════
   BOTONES STREAMLIT
   ══════════════════════════════════════════════ */
[data-testid="stButton"] > button {
    background: var(--accent) !important;
    color: white !important;
    border: none !important;
    border-radius: var(--radius) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.875rem !important;
    font-weight: 600 !important;
    padding: 0.65rem 1.4rem !important;
    box-shadow: 0 1px 3px rgba(37,99,235,0.25), 0 0 0 0 rgba(37,99,235,0) !important;
    transition: all 0.15s !important;
    letter-spacing: 0.01em !important;
    width: 100% !important;
}

[data-testid="stButton"] > button:hover {
    background: #1d4ed8 !important;
    box-shadow: 0 4px 12px rgba(37,99,235,0.3) !important;
    transform: translateY(-1px) !important;
}

[data-testid="stDownloadButton"] > button {
    background: var(--surface) !important;
    color: var(--text-2) !important;
    border: 1px solid var(--border-md) !important;
    border-radius: var(--radius) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.875rem !important;
    font-weight: 600 !important;
    padding: 0.65rem 1.4rem !important;
    transition: all 0.15s !important;
    width: 100% !important;
}

[data-testid="stDownloadButton"] > button:hover {
    border-color: var(--accent) !important;
    color: var(--accent) !important;
    background: var(--accent-bg) !important;
}

/* ══════════════════════════════════════════════
   EXPANDER
   ══════════════════════════════════════════════ */
[data-testid="stExpander"] {
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
    background: var(--surface) !important;
    margin-bottom: 0.5rem !important;
    box-shadow: none !important;
}

[data-testid="stExpander"] summary {
    font-size: 0.84rem !important;
    font-weight: 600 !important;
    color: var(--text-2) !important;
    padding: 0.7rem 1rem !important;
    font-family: 'DM Sans', sans-serif !important;
}

[data-testid="stExpander"] summary:hover { color: var(--accent) !important; }

/* ══════════════════════════════════════════════
   SELECTBOX
   ══════════════════════════════════════════════ */
[data-testid="stSelectbox"] label {
    font-size: 0.8rem !important;
    font-weight: 600 !important;
    color: var(--text-3) !important;
    text-transform: uppercase !important;
    letter-spacing: 0.05em !important;
}

[data-testid="stSelectbox"] > div > div {
    background: var(--surface) !important;
    border: 1px solid var(--border-md) !important;
    border-radius: var(--radius) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.92rem !important;
    color: var(--text-1) !important;
    box-shadow: var(--shadow-sm) !important;
}

[data-testid="stSelectbox"] > div > div:focus-within {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px rgba(37,99,235,0.1) !important;
}

/* ══════════════════════════════════════════════
   TABS
   ══════════════════════════════════════════════ */
[data-testid="stTabs"] [role="tablist"] {
    background: var(--bg) !important;
    border-radius: var(--radius) !important;
    border: 1px solid var(--border) !important;
    padding: 3px !important;
    gap: 2px !important;
}

[data-testid="stTabs"] [role="tab"] {
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    color: var(--text-3) !important;
    border-radius: var(--radius-sm) !important;
    padding: 0.45rem 0.85rem !important;
    border: none !important;
    transition: all 0.12s !important;
}

[data-testid="stTabs"] [role="tab"][aria-selected="true"] {
    background: var(--surface) !important;
    color: var(--text-1) !important;
    font-weight: 600 !important;
    box-shadow: var(--shadow-sm) !important;
}

/* ══════════════════════════════════════════════
   SUCCESS / INFO / ERROR
   ══════════════════════════════════════════════ */
[data-testid="stSuccess"] {
    background: var(--success-bg) !important;
    border: 1px solid #bbf7d0 !important;
    border-radius: var(--radius) !important;
    color: #14532d !important;
    font-size: 0.86rem !important;
}

[data-testid="stInfo"] {
    background: var(--accent-bg) !important;
    border: 1px solid #bfdbfe !important;
    border-radius: var(--radius) !important;
    color: #1e3a5f !important;
    font-size: 0.86rem !important;
}

[data-testid="stAlert"] {
    border-radius: var(--radius) !important;
    font-size: 0.86rem !important;
}

/* ══════════════════════════════════════════════
   SCROLLBAR
   ══════════════════════════════════════════════ */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border-md); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--text-4); }

/* ══════════════════════════════════════════════
   OCULTAR CHROME STREAMLIT
   ══════════════════════════════════════════════ */
#MainMenu, footer, [data-testid="stToolbar"] { visibility: hidden; }

/* ══════════════════════════════════════════════
   DIVIDER
   ══════════════════════════════════════════════ */
hr {
    border: none !important;
    border-top: 1px solid var(--border) !important;
    margin: 1.5rem 0 !important;
}

/* ══════════════════════════════════════════════
   ESTADO INICIAL — GRID DE MÓDULOS
   ══════════════════════════════════════════════ */
.modules-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.7rem;
    margin-top: 1rem;
}

.module-preview {
    background: var(--bg);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 1rem;
    display: flex;
    gap: 0.7rem;
    align-items: flex-start;
}

.module-preview-icon {
    width: 34px;
    height: 34px;
    border-radius: var(--radius-sm);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    flex-shrink: 0;
}

.module-preview-title {
    font-size: 0.8rem;
    font-weight: 700;
    color: var(--text-1);
    margin-bottom: 0.15rem;
}

.module-preview-desc {
    font-size: 0.78rem;
    color: var(--text-3);
    line-height: 1.5;
}

/* ══════════════════════════════════════════════
   SPINNER OVERRIDE
   ══════════════════════════════════════════════ */
[data-testid="stSpinner"] p {
    font-size: 0.85rem !important;
    color: var(--text-3) !important;
}
</style>
""", unsafe_allow_html=True)