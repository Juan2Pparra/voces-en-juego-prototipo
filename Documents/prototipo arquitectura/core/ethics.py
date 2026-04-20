REGLAS_ETICAS = [
    "No reproducir descripciones de violencia explícita.",
    "No revictimizar ni reducir a las personas a su sufrimiento.",
    "Respetar la fidelidad contextual del relato original.",
    "No estigmatizar comunidades ni grupos sociales.",
    "No romantizar actores armados ni la guerra.",
    "Proteger la voz de la infancia y de poblaciones vulnerables.",
    "Usar un tono respetuoso, reflexivo y digno.",
]


def modulo_1_4_control_etico(historia: dict, blueprint: dict) -> dict:
    titulo = historia.get("titulo", "Historia sin título")
    resumen = historia.get("resumen", "")
    fragmento = blueprint["fragmento_base"]
    ubicacion = blueprint["ubicacion"]
    actores = ", ".join(blueprint["actores"]) if blueprint["actores"] else "actores del conflicto"
    temas = ", ".join(blueprint["temas"]) if blueprint["temas"] else "conflicto armado"

    reglas_str = "\n".join(f"- {r}" for r in REGLAS_ETICAS)

    prompt = f"""
Eres un diseñador narrativo de un videojuego educativo sobre memoria histórica del conflicto armado en Colombia.

HISTORIA BASE:
- Título: {titulo}
- Resumen: {resumen}
- Ubicación: {ubicacion}
- Actores: {actores}
- Temas: {temas}
- Emoción principal: {blueprint['emocion_principal']}
- Emoción secundaria: {blueprint['emocion_secundaria']}
- Fragmento testimonial original: "{fragmento}"

BLUEPRINT NARRATIVO:
- Tipo de escena: {blueprint['tipo_escena']}
- Tono: {blueprint['tono']}
- Objetivo narrativo: {blueprint['objetivo_narrativo']}

RESTRICCIONES ÉTICAS (OBLIGATORIAS):
{reglas_str}

TAREA:
Genera contenido narrativo en español, de forma concisa y clara:

1. ESCENA (máximo 5 oraciones): describe el ambiente y la situación.
2. DIÁLOGO NPC (máximo 4 líneas): una voz testimonial o comunitaria, auténtica y digna.
3. DECISIONES (exactamente 3 opciones): opciones del jugador con consecuencias narrativas o morales distintas.

Responde ÚNICAMENTE con este formato exacto:

### ESCENA
...

### DIÁLOGO NPC
...

### DECISIONES
A) ...
B) ...
C) ...
""".strip()

    return {
        "reglas_eticas": REGLAS_ETICAS,
        "prompt_construido": prompt,
    }