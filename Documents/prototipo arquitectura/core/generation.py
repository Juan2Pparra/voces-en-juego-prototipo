"""
core/generation.py
Módulo 1.5 – Generación narrativa.
Usa la API de Anthropic si ANTHROPIC_API_KEY está disponible.
Si no, usa un generador local estructurado como fallback.
"""

import os
import random
from typing import Dict

# ─────────────────────────────────────────────────────
# PARSER DE RESPUESTA CLAUDE
# ─────────────────────────────────────────────────────

def parsear_respuesta_claude(texto: str) -> Dict[str, str]:
    """Extrae escena, diálogo y decisiones del texto de Claude."""
    lineas_escena, lineas_dialogo, lineas_decisiones = [], [], []
    seccion = None

    for linea in texto.splitlines():
        s = linea.strip()
        upper = s.upper()
        if "### ESCENA" in upper:
            seccion = "escena"
        elif "### DIÁLOGO NPC" in upper or "### DIALOGO NPC" in upper:
            seccion = "dialogo"
        elif "### DECISIONES" in upper:
            seccion = "decisiones"
        elif s:
            if seccion == "escena":
                lineas_escena.append(s)
            elif seccion == "dialogo":
                lineas_dialogo.append(s)
            elif seccion == "decisiones":
                lineas_decisiones.append(s)

    return {
        "escena":      " ".join(lineas_escena).strip(),
        "dialogo_npc": "\n".join(lineas_dialogo).strip(),
        "decisiones":  "\n".join(lineas_decisiones).strip(),
        "texto_completo": texto,
        "modo": "api",
    }


# ─────────────────────────────────────────────────────
# GENERADOR LOCAL (fallback sin API)
# ─────────────────────────────────────────────────────

_ESCENAS = {
    "miedo": [
        "En {ubicacion}, el jugador entra en una escena de tensión contenida donde el silencio pesa más que las palabras. "
        "El ambiente sugiere incertidumbre pero también una voluntad colectiva de seguir adelante. "
        "La narrativa gira en torno a {actor} y su experiencia con {tema}. "
        "El propósito de la escena es {objetivo}.",
        "Las calles de {ubicacion} guardan un silencio que la comunidad aprendió a leer. "
        "{actor} observa el horizonte con la parsimonia de quien ha visto demasiado. "
        "La escena transmite cómo el miedo puede coexistir con la resistencia. "
        "El objetivo narrativo es {objetivo}.",
    ],
    "tristeza": [
        "En {ubicacion}, la escena se construye desde la memoria y la ausencia. "
        "{actor} sostiene un objeto cotidiano que ahora pesa diferente. "
        "El tono íntimo y reflexivo guía al jugador hacia una comprensión del duelo sin sensacionalismo. "
        "El propósito es {objetivo}.",
        "La habitación en {ubicacion} huele a ausencia. "
        "{actor} no pide lástima; pide que alguien recuerde junto a ella. "
        "La escena centra su mirada en {tema} con un tono solemne y contemplativo. "
        "Objetivo: {objetivo}.",
    ],
    "sorpresa": [
        "Nadie esperaba que en {ubicacion} las cosas cambiaran tan rápido. "
        "{actor} debe procesar una revelación que transforma la comprensión de lo vivido. "
        "La escena gira en torno a {tema} con urgencia y apertura reflexiva. "
        "Propósito: {objetivo}.",
    ],
    "neutral": [
        "En {ubicacion}, la vida sigue su curso con la parsimonia de quien aprendió a resistir. "
        "{actor} está sentado frente al jugador, listo para hablar. "
        "Debajo de esa normalidad hay capas de historia relacionadas con {tema}. "
        "El propósito es {objetivo}.",
    ],
    "molestia": [
        "La comunidad de {ubicacion} lleva años pidiendo lo mismo. "
        "{actor} habla con la claridad de quien ya no tiene paciencia para los rodeos. "
        "La escena se articula desde una voz crítica sobre {tema}. "
        "Objetivo narrativo: {objetivo}.",
    ],
    "decepción": [
        "En {ubicacion}, la promesa no cumplida dejó una huella que {actor} carga con lucidez. "
        "La escena muestra desgaste sin perder la posibilidad de reflexión sobre {tema}. "
        "El tono es amargo pero constructivo. Propósito: {objetivo}.",
    ],
    "aprobación": [
        "En {ubicacion}, {actor} y su comunidad lograron algo que nadie habría imaginado solo. "
        "La escena resalta la solidaridad y el poder de los vínculos colectivos en torno a {tema}. "
        "Objetivo: {objetivo}.",
    ],
    "alegría": [
        "El espacio de {ubicacion} es la memoria viva de un pueblo que se negó a desaparecer. "
        "{actor} cuenta historias que los jóvenes aprenden a atesorar. "
        "La escena celebra la resistencia cultural vinculada a {tema}. "
        "Propósito: {objetivo}.",
    ],
    "desaprobación": [
        "La historia de {ubicacion} cuestiona lo que se daba por sentado. "
        "{actor} ofrece un testimonio que obliga al jugador a revisar sus propias certezas sobre {tema}. "
        "El tono es filosófico y digno. Objetivo: {objetivo}.",
    ],
}

_DIALOGOS = {
    "maternidad":     ["Hay dolores que una madre no deja atrás, pero sí aprende a convertir en memoria.",
                       "No busco respuestas perfectas, solo que su historia no sea olvidada."],
    "pérdida":        ["Lo que se pierde no desaparece; a veces permanece en la forma en que seguimos nombrándolo.",
                       "La ausencia cambia todo, pero también nos obliga a recordar con más fuerza."],
    "proceso de paz": ["Hablar de paz no siempre significa que el miedo haya terminado.",
                       "La paz también necesita memoria, no solo silencios."],
    "conflicto":      ["Lo vivido aquí no puede reducirse a una sola versión de los hechos.",
                       "Cada historia del conflicto deja marcas distintas en quienes la vivieron."],
    "familia":        ["En la familia aprendimos a recordar sin dejar que el dolor fuera lo único que quedara.",
                       "La memoria familiar también es una forma de resistencia."],
    "cultura":        ["Lo que somos como comunidad vive en aquello que insistimos en preservar.",
                       "Nuestra cultura no desaparece mientras alguien siga contándola."],
    "identidad":      ["Nadie puede quitarnos lo que somos si nosotros decidimos seguir siendo.",
                       "La identidad no es un dato; es una práctica cotidiana de resistencia."],
    "resistencia":    ["Quedarse también fue una decisión. No todos la entienden, pero fue nuestra.",
                       "Resistir no siempre se ve. A veces solo significa seguir aquí."],
}

_DECISIONES = {
    "duelo":          ("A) Escuchar sin interrumpir y acompañar el relato.",
                       "B) Preguntar qué significa recordar en medio de la pérdida.",
                       "C) Preguntar cómo la comunidad ha acompañado ese proceso."),
    "proceso de paz": ("A) Preguntar qué cambió realmente para la comunidad.",
                       "B) Preguntar qué temores persisten pese a hablar de paz.",
                       "C) Preguntar qué significa reconstruir la confianza."),
    "familia":        ("A) Preguntar cómo cambió la vida familiar después de lo ocurrido.",
                       "B) Escuchar el recuerdo y acompañar en silencio.",
                       "C) Preguntar qué quieren preservar de esa memoria."),
    "cultura":        ("A) Preguntar por el significado cultural de lo que se está contando.",
                       "B) Preguntar cómo la comunidad protege esa memoria.",
                       "C) Pedir que continúe el relato desde su propia voz."),
    "conflicto":      ("A) Preguntar por el contexto de lo ocurrido.",
                       "B) Preguntar cómo afectó a la comunidad en su vida cotidiana.",
                       "C) Preguntar qué aprendizaje deja esa experiencia."),
    "resistencia":    ("A) Preguntar qué estrategias usó la comunidad para mantenerse.",
                       "B) Preguntar a quiénes reconocen como referentes de resistencia.",
                       "C) Preguntar qué le dirían hoy a quienes aún no han podido resistir."),
    "identidad":      ("A) Preguntar qué prácticas mantienen viva la identidad colectiva.",
                       "B) Preguntar qué cambió en la identidad después del conflicto.",
                       "C) Preguntar qué quieren transmitir a las próximas generaciones."),
}

_DEFAULT_DECISIONES = (
    "A) Escuchar con atención y pedir que continúe el relato.",
    "B) Preguntar cómo afectó a su comunidad lo que describe.",
    "C) Preguntar qué quisiera que el jugador aprendiera de su historia.",
)


def _generar_local(historia: dict, blueprint: dict) -> Dict[str, str]:
    """Generador local estructurado que usa los atributos del JSON."""
    emocion   = blueprint.get("emocion_principal", "neutral")
    temas     = blueprint.get("temas", [])
    actores   = blueprint.get("actores", [])
    ubicacion = blueprint.get("ubicacion", "Colombia")
    objetivo  = blueprint.get("objetivo_narrativo", "generar reflexión sobre el conflicto")

    tema_str  = temas[0].lower() if temas else "conflicto"
    actor_str = actores[0] if actores else "un habitante de la comunidad"

    # Escena
    plantillas = _ESCENAS.get(emocion, _ESCENAS["neutral"])
    escena = random.choice(plantillas).format(
        ubicacion=ubicacion,
        actor=actor_str,
        tema=tema_str,
        objetivo=objetivo.lower(),
    )

    # Diálogo NPC — busca el tema más específico primero
    dialogo = None
    for t in temas:
        opts = _DIALOGOS.get(t.lower())
        if opts:
            dialogo = random.choice(opts)
            break
    if not dialogo:
        dialogo = random.choice(_DIALOGOS["conflicto"])

    # Decisiones — busca el tema más específico
    decisiones_tuple = None
    for t in temas:
        decisiones_tuple = _DECISIONES.get(t.lower())
        if decisiones_tuple:
            break
    if not decisiones_tuple:
        decisiones_tuple = _DEFAULT_DECISIONES

    return {
        "escena":      escena,
        "dialogo_npc": dialogo,
        "decisiones":  "\n".join(decisiones_tuple),
        "texto_completo": f"[generación local]\n\nESCENA:\n{escena}\n\nDIÁLOGO NPC:\n{dialogo}\n\nDECISIONES:\n" + "\n".join(decisiones_tuple),
        "modo": "local",
    }


# ─────────────────────────────────────────────────────
# FUNCIÓN PRINCIPAL DEL MÓDULO
# ─────────────────────────────────────────────────────

def modulo_1_5_generacion(prompt: str, historia: dict, blueprint: dict) -> dict:
    """
    Intenta usar la API de Anthropic.
    Si no hay API key disponible, usa el generador local como fallback.
    """
    api_key = os.getenv("ANTHROPIC_API_KEY", "").strip()

    if not api_key:
        return _generar_local(historia, blueprint)

    try:
        from anthropic import Anthropic
        client = Anthropic(api_key=api_key)
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=900,
            messages=[{"role": "user", "content": prompt}],
        )
        texto = response.content[0].text.strip()
        return parsear_respuesta_claude(texto)

    except Exception as e:
        # Si falla la API por cualquier razón, cae al generador local
        resultado = _generar_local(historia, blueprint)
        resultado["error_api"] = str(e)
        return resultado