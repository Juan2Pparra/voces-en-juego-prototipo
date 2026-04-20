import re
from core.codesign import normalizar


PALABRAS_ALERTA = [
    "sangre", "matar", "asesin", "tortur", "violar", "cadáver",
    "pobrecito", "pobrecita", "víctima patética", "héroe armado",
    "explosión", "balacera", "masacre detallada",
]

PALABRAS_POSITIVAS = [
    "dignidad", "memoria", "comunidad", "resistencia", "esperanza",
    "familia", "paz", "reconocimiento", "futuro", "reconstruir",
]


def modulo_1_6_validacion(generado: dict, blueprint: dict, historia: dict) -> dict:
    texto_total = (
        generado["escena"] + " " +
        generado["dialogo_npc"] + " " +
        generado["decisiones"]
    ).lower()

    observaciones = []
    alertas = []
    puntuacion = 100

    temas_historia = [normalizar(t) for t in historia.get("temas", [])]
    temas_encontrados = sum(1 for t in temas_historia if t in texto_total)
    coherencia_score = round((temas_encontrados / max(len(temas_historia), 1)) * 100)

    if coherencia_score < 40:
        observaciones.append(f"⚠️ Baja coherencia temática ({coherencia_score}%).")
        puntuacion -= 20
    else:
        observaciones.append(f"✅ Coherencia temática aceptable ({coherencia_score}%).")

    ubicacion = normalizar(historia.get("ubicacion") or "")
    if ubicacion and ubicacion not in texto_total:
        observaciones.append(f"ℹ️ La ubicación '{historia.get('ubicacion')}' no aparece explícitamente.")

    encontradas = [p for p in PALABRAS_ALERTA if p in texto_total]
    if encontradas:
        alertas.append(f"⚠️ Riesgo ético: {', '.join(encontradas[:5])}.")
        puntuacion -= 15 * len(encontradas[:3])

    positivos = [p for p in PALABRAS_POSITIVAS if p in texto_total]
    if positivos:
        observaciones.append(f"✅ Elementos positivos detectados: {', '.join(positivos[:4])}.")
    else:
        observaciones.append("ℹ️ Se recomienda reforzar dignidad, comunidad o esperanza.")
        puntuacion -= 10

    lineas_dec = [l for l in generado["decisiones"].splitlines() if l.strip()]
    if len(lineas_dec) < 3:
        alertas.append(f"⚠️ Se esperaban 3 decisiones y se generaron {len(lineas_dec)}.")
        puntuacion -= 10
    else:
        observaciones.append("✅ Tres decisiones generadas correctamente.")

    fragmento_base = normalizar(blueprint["fragmento_base"])
    palabras_frag = [p for p in re.findall(r"\w+", fragmento_base) if len(p) > 4][:5]
    fidelidad_ok = any(p in texto_total for p in palabras_frag) if palabras_frag else True

    if fidelidad_ok:
        observaciones.append("✅ Fidelidad contextual aceptable respecto al fragmento base.")
    else:
        observaciones.append("ℹ️ No se detectó referencia clara al fragmento base.")

    puntuacion = max(0, min(100, puntuacion))

    if puntuacion >= 80:
        estado = "✅ APROBADO"
        color = "green"
    elif puntuacion >= 55:
        estado = "⚠️ REVISAR"
        color = "orange"
    else:
        estado = "❌ REQUIERE CORRECCIÓN"
        color = "red"

    return {
        "puntuacion": puntuacion,
        "estado": estado,
        "color": color,
        "observaciones": observaciones,
        "alertas": alertas,
    }