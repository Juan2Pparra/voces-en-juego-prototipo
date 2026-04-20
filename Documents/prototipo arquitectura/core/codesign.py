def normalizar(texto):
    return str(texto).strip().lower()


TIPO_ESCENA = {
    "miedo": "Escena de tensión y resistencia",
    "tristeza": "Escena de duelo y memoria",
    "sorpresa": "Escena de quiebre y revelación",
    "neutral": "Escena de testimonio reflexivo",
    "decepción": "Escena de desilusión y búsqueda de sentido",
    "molestia": "Escena de denuncia y reclamo",
    "aprobación": "Escena de solidaridad comunitaria",
    "alegría": "Escena de resistencia cultural",
    "desaprobación": "Escena de cuestionamiento moral",
}

TONO_POR_EMOCION = {
    "miedo": "tenso, íntimo y esperanzador",
    "tristeza": "melancólico, solemne y contemplativo",
    "sorpresa": "desconcertante, urgente y reflexivo",
    "neutral": "sobrio, documental y digno",
    "decepción": "amargo, introspectivo y en búsqueda de salida",
    "molestia": "directo, crítico y empoderado",
    "aprobación": "cálido, comunitario y esperanzador",
    "alegría": "vibrante, orgulloso y resiliente",
    "desaprobación": "cuestionador, filosófico y digno",
}

OBJETIVO_POR_TEMA = {
    "conflicto": "Que el jugador comprenda el impacto humano del conflicto sin glorificar la violencia",
    "proceso de paz": "Reflexionar sobre la paz como proceso colectivo frágil y necesario",
    "estigmatización": "Generar empatía hacia comunidades estigmatizadas",
    "miedo": "Mostrar la resistencia frente al terror sin reproducirlo",
    "resistencia": "Valorar estrategias de supervivencia comunitaria",
    "comunidad": "Comprender el poder de la acción colectiva",
    "duelo": "Acompañar el proceso de duelo con dignidad",
    "espiritualidad": "Respetar formas de sentido y sanación no occidentales",
    "familia": "Reconocer el rol de la familia en la memoria histórica",
    "reclutamiento": "Visibilizar el reclutamiento como violación de derechos",
    "infancia": "Proteger la narrativa de la infancia afectada",
    "violencia familiar": "Abordar el abuso con sensibilidad sin revictimizar",
    "intuición": "Explorar la dimensión emocional de la pérdida anticipada",
    "pérdida": "Reconocer el impacto humano de la violencia en las familias",
    "maternidad": "Honrar la experiencia materna en contextos de conflicto",
    "suicidio": "Tratar la desesperanza con cuidado ético y apertura al sentido",
    "desesperanza": "Abrir caminos simbólicos de reconstrucción",
    "cultura": "Valorar la diversidad cultural como resistencia",
    "identidad": "Fortalecer el reconocimiento de identidades marginadas",
    "lengua": "Visibilizar la pérdida lingüística como violencia simbólica",
    "masacres": "Recordar con dignidad sin reproducir el horror",
    "racismo": "Evidenciar el racismo estructural",
    "abandono estatal": "Cuestionar la responsabilidad institucional",
    "dolor": "Humanizar a las víctimas en toda su complejidad",
    "paro nacional": "Entender la protesta como expresión de ciudadanía",
    "solidaridad": "Inspirar acciones de cuidado comunitario",
    "salud": "Reconocer la salud como derecho en contextos de crisis",
    "paz territorial": "Construir comprensión de la paz desde los territorios",
    "educación forzada": "Denunciar la violencia cultural institucional",
    "maltrato": "Visibilizar el abuso sin reproducirlo",
    "desarraigo": "Generar empatía hacia comunidades desplazadas",
    "religión": "Reflexionar sobre imposición religiosa y colonialidad",
    "colonialidad": "Cuestionar estructuras históricas de poder",
}

EMOCION_EMOJI = {
    "miedo": "😰",
    "tristeza": "💧",
    "sorpresa": "⚡",
    "neutral": "🌿",
    "decepción": "🌧️",
    "molestia": "🔥",
    "aprobación": "🤝",
    "alegría": "🌻",
    "desaprobación": "⚖️",
}


def modulo_1_3_codiseno(historia: dict) -> dict:
    emocion = historia.get("emocion_principal", {}).get("emocion", "neutral")
    temas = historia.get("temas", [])
    primer_tema = normalizar(temas[0]) if temas else "conflicto"

    tipo_escena = TIPO_ESCENA.get(emocion, "Escena de testimonio")
    tono = TONO_POR_EMOCION.get(emocion, "sobrio y digno")
    objetivo = OBJETIVO_POR_TEMA.get(primer_tema, "Generar reflexión sobre el conflicto colombiano")

    return {
        "tipo_escena": tipo_escena,
        "tono": tono,
        "objetivo_narrativo": objetivo,
        "emocion_principal": emocion,
        "emocion_secundaria": historia.get("emocion_secundaria", {}).get("emocion", ""),
        "temas": historia.get("temas", []),
        "actores": historia.get("actores", []),
        "ubicacion": historia.get("ubicacion") or "Colombia",
        "fragmento_base": historia.get("fragmentos", [""])[0] if historia.get("fragmentos") else "",
    }